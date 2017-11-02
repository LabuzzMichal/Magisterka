/// **********************************************************************
/////
///// Use a root file with monitoring histograms to fetch various features
///// for ML training
/////
///// **********************************************************************

#include<string>
#include<iostream>
#include<TROOT.h>




void preprocessData(std::string fname, std::string catalogue, bool deb = false){
  cout<<catalogue<<endl;
  TString params = "" ;  
  TString params_i = "";
  gROOT->Reset();
  bool isDebug = deb;

  TFile * f = new TFile(fname.c_str(), "READ");
  if( f->IsZombie() ){

    printf( " file is corrupted! \n" );
    f = NULL;
    //exit();

  }


  std::string vetra("Vetra");
  std::string pedmoni("VeloPedestalSubtractorMoni");
  std::string peddir = vetra + "/" + pedmoni;

  TDirectory* tell1s = NULL;
  tell1s = (TDirectory*)f->Get(peddir.c_str());

  int substring = 6;

  TIter next( tell1s->GetListOfKeys() );
  TKey* aKey = NULL;

  Int_t isensor(-999);
  Double_t mean(0.), rms(0.), ske(0.), kur(0.);

  std::string hName = "Ped_Sub_ADCs_2D";

  while( (aKey = (TKey*)next()) ){

    if( aKey->IsFolder() ){

      tell1s->cd( aKey->GetName() );
      //printf( " entering the %s directory \n", aKey->GetName() );
      std::string name = aKey->GetName();
      std::string ssensor = name.substr( substring );
      isensor = atoi( ssensor.c_str() );

      if( isDebug ) printf( " sensor string %s \n", ssensor.c_str() );
      if( isDebug ) printf( " sensor number is: %i \n", isensor );

      TH2D* aPedHist = (TH2D*)gDirectory->Get( hName.c_str() );
      if( aPedHist == NULL ){

        printf( " Having problem with sensor: %i, probably this one is missing... \n", isensor );
        continue;

      }
      TH1D* aNoiseHist = aPedHist->ProjectionY();
      if( aNoiseHist == NULL ){

        printf( " Problem with projection of the data from sensor: %i \n", isensor );
        continue;

      }
      //TCanvas * cv = new TCanvas();
      //aNoiseHist->DrawCopy();
      //std::string pre = "../Fig/" + catalogue + "/";
      //std::string post = "_noseDistr.png";
      //std::string path = pre + ssensor + post;     
      //cv->SaveAs(path.c_str());
        
      mean = aNoiseHist->GetMean();
      rms = aNoiseHist->GetRMS();
      ske = aNoiseHist->GetSkewness();
      kur = aNoiseHist->GetKurtosis();
      
      params_i.Form("%f,%f,%f,%f,1.0\n", mean, rms, ske, kur);
      params.Append(params_i);     

      if( isDebug ) printf( " M: %f, RMS: %f, Sk: %f, Ku: %f for sensor %i \n", mean, rms, ske, kur, isensor );
    //cv->Clear();
    //delete cv;
    delete aNoiseHist;
    delete aPedHist;
    }

  }
  f = NULL;
  delete f;

  ofstream myfile;
  myfile.open("../Data/sensorData" + catalogue + ".dat");
  myfile << params;
  myfile.close();
  
}

void iterate(){
   gSystem->Exec("./bash_script");
   ifstream infile("list.txt");
   std::string line;
   std::string folder;
   while (std::getline(infile,line)){
     folder = line.substr(line.size()-35,6);
     std::string path2 = "../Fig/"+folder;
     gSystem->mkdir(path2.c_str());
     preprocessData(line,folder,0);

   }
   //preprocessData("/home/mlabuz/Desktop/Projekt/Data/180000s/180000s/180300s/180369/VELODQM_180369_2016-07-21_11.15.15_NZS.root","180369",1);
   
}


