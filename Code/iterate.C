{
   gSystem->Exec("./bash_script");
   ifstream infile("list.txt");
   std::string line;
   while (std::getline(infile,line)){
     cout << line << endl;
     cout << line.substr(line.size()-35,6) <<endl;
   }
}
