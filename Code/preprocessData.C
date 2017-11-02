{
  gROOT->Reset();
  // data file
  TFile * f = new TFile("../Data/180000s/180000s/180500s/180596/VELODQM_180596_2016-07-25_07.30.48_NZS.root");
  // sub-catalogue -- seperate for each data-set
  TString CATALOGUE("180596");

  // there are 41 sensors total
  const int lastSensorId = 41;

//  TCanvas * cv = new TCanvas();


  TString sensorId;
  TString params; // [lastSensorId + 1];
  TString params_i;
  
  // histogram handles
  TH2D* h2d;
  TH1D* noiseDistr;

  for (int i = 0; i <= lastSensorId; i++) 
  {
    cout << i << endl;
    //TCanvas * cv = new TCanvas();
    //cv->Clear();
    
    // refresh default sensor name
    TString sensorName("TELL1_000");

    // set sensor name so it corresponds to the loop index
    sensorId.Form("%d", i);
    sensorName.Replace(sensorName.Sizeof() - sensorId.Sizeof(), sensorId.Sizeof(), sensorId);
    cout << "Working on sensor: " << sensorName << endl;

    // go to sensor's location (inside the ROOT file)
    if (!(f->cd("Vetra;1/VeloPedestalSubtractorMoni/" + sensorName + ";1"))) {
      cout << "Couldn't find sensor: " << sensorName << endl;
      break;
    }
    
    h2d =  Ped_Sub_ADCs_2D;

    cout << "1d hists now" << endl;

    noiseDistr = h2d->ProjectionY("_py", 0, -1, ""); 

    //noiseDistr->DrawCopy();
    //cv->SaveAs(sensorName + "_noiseDistr" + ".png");

    // get statistical params of the noise distribution
    double mu, sig, skew, kur, quality;
    mu = noiseDistr->GetMean();
    sig = noiseDistr->GetRMS();
    skew = noiseDistr->GetSkewness();
    kur = noiseDistr->GetKurtosis();

    // sensor quality 0 or 1 for now;
    quality = 1.0;  // assume all are OK. Otherwise, if there a few bad ones, you can adjust them manually in the output file


    params_i.Form("%f,%f,%f,%f,%f\n", mu, sig, skew, kur, quality);
    params.Append(params_i);

    //cv->Clear();
    //delete h2d;
    // delete noiseDistr;
  }
cout << params;
ofstream myfile;
myfile.open("../Data/sensorData" + CATALOGUE+ ".dat");
myfile << params;
myfile.close();
}



