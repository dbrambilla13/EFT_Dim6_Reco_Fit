vector <float>
getLSintersections (TGraph * graphScan, float val)
{
  vector <float> xings ;
  int n = graphScan->GetN () ;
  double * x = graphScan->GetX () ;
  double * y = graphScan->GetY () ;
  bool found = false ;
  pair<float, float> around ;
  // loop over tgraph points
  for (int i = 1 ; i < n ; ++i)
    {
      if (y[i] == val) 
        {
          xings.push_back (x[i]) ;
          continue ;
        }  
      // notice a crossing 
      if ((y[i] - val) * (y[i-1] - val) < 0)
        {
          xings.push_back (x[i-1] +  fabs ((y[i-1] - val) * (x[i] - x[i-1]) / (y[i] - y[i-1])) ) ;
        }
    }  // loop over tgraph points

  if (xings.size () == 0)
    { 
      cout << "WARNING: returning graph x-axis range limits" << endl ;
      xings.push_back (graphScan->GetXaxis ()->GetXmin ()) ;
      xings.push_back (graphScan->GetXaxis ()->GetXmax ()) ;
    }
  else if (xings.size () == 1)
    {
      if (xings.back () < 0) 
        {
          cout << "WARNING: returning graph x-axis higher limit" << endl ;
          xings.push_back (graphScan->GetXaxis ()->GetXmax ()) ;
        }
      else 
        {
          cout << "WARNING: returning graph x-axis lower limit" << endl ;
          xings.push_back (xings.back ()) ;
          xings.at (0) = graphScan->GetXaxis ()->GetXmin () ;
        }
    }
  if (xings.size () > 2) 
    {
      cout << "WARNING: more than two intersections found, returning the first two" << endl ;
      xings.resize (2) ;

    }
  return xings ;
}  


void draw_v1(std::string variable = "k_my_1",std::string var_name = "default") {
  
  TCanvas* cc = new TCanvas("cc","", 800, 600);
  int n = 0;
  int n_data = 0;
  
  TTree* limit = (TTree*) _file0->Get("limit");  
  //   n = limit->Draw("2*deltaNLL:r","deltaNLL<10 && deltaNLL>-30","l");
  
  TString toDraw = Form("2*deltaNLL:%s", variable.c_str());
  
  n = limit->Draw( toDraw.Data() , "deltaNLL<50 && deltaNLL>-30", "l");
  TGraph *graphScan = new TGraph(n,limit->GetV2(),limit->GetV1());
  graphScan->RemovePoint(0);
  
  TGraph *graphScanData = 0;
  TTree* limitData = (TTree*) _file1->Get("limit");  
  //     n_data = limitData->Draw("2*deltaNLL:r","deltaNLL<40 && deltaNLL>-30","l");
  n_data = limitData->Draw(  toDraw.Data() , "deltaNLL<50 && deltaNLL>-30", "l");
  graphScanData = new TGraph(n_data,limitData->GetV2(),limitData->GetV1());
  graphScanData->RemovePoint(0);
  graphScanData->SetTitle("");
  graphScanData->SetMarkerStyle(21);
  graphScanData->SetLineWidth(2);
  graphScanData->SetMarkerColor(kRed);
  graphScanData->SetLineColor(kRed);
  
  cc->SetGrid();
  
  
  graphScan->SetTitle("");
  graphScan->SetMarkerStyle(21);
  graphScan->SetLineWidth(2);
  graphScan->SetMarkerColor(kBlue);
  graphScan->SetLineColor(kBlue);
  
  //   graphScan->Draw("APL");
  
  //----
  cc->SetTicks();
  cc->SetFillColor(0);
  cc->SetBorderMode(0);
  cc->SetBorderSize(2);
  cc->SetTickx(1);
  cc->SetTicky(1);
  cc->SetRightMargin(0.05);
  cc->SetBottomMargin(0.12);
  cc->SetFrameBorderMode(0);
  
  TLatex * tex;
  tex = new TLatex(0.94,0.92,"13 TeV");
  tex->SetNDC();
  tex->SetTextAlign(31);
  tex->SetTextFont(42);
  tex->SetTextSize(0.04);
  tex->SetLineWidth(2);
  
  TLatex * tex2 = new TLatex(0.14,0.92,"CMS");
  tex2->SetNDC();
  tex2->SetTextFont(61);
  tex2->SetTextSize(0.04);
  tex2->SetLineWidth(2);
  
  TLatex * tex3;
  tex3 = new TLatex(0.236,0.92,"L = XX fb^{-1}  Preliminary");
  tex3->SetNDC();
  tex3->SetTextFont(52);
  tex3->SetTextSize(0.035);
  tex3->SetLineWidth(2);
  
  
  float minX = 999;
  float maxX = -999;
  
  
  //---- clean duplicate (it happens during lxbatch scan)
  std::vector <double> x_std;
  std::map <double, double> x_y_map;
  double x_value;
  double y_value;
  for (int ip = 0; ip<graphScan->GetN(); ip++) {
    
    graphScan->GetPoint (ip, x_value, y_value);
    //     std::cout << " x_value = " << x_value << std::endl;
    if (std::find(x_std.begin(), x_std.end(), x_value) != x_std.end()) {
      graphScan->RemovePoint(ip);
      //       std::cout << "removed " << ip << std::endl;
      ip--;
    }
    else {
      x_std.push_back(x_value);
      x_y_map[x_value] = y_value;
    }
  }
  
  graphScan->Set(0);
  
  
  float mc_min_x = -100;
  //---- fix the 0 of the likelihood scan
  float minimum = 1000;
  for (std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
    if ( it->second < minimum ) {
      minimum = it->second;
      mc_min_x = it->first;
    }
  }
  for (std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
    it->second =  it->second - minimum;
  }
  //---- (end) fix the 0 of the likelihood scan
  
  
  int ip = 0;
  for (std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
    graphScan->SetPoint( ip, it->first , it->second);
    ip++;
  }
  
  
  //---- just for horizonthal lines
  for (std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
    if ( it->first < minX ) {
      minX = it->first;
    }
    if ( it->first > maxX ) {
      maxX = it->first;
    }
  }
  //---- (end) just for horizonthal lines
  
  
  
  
  
  
  x_std.clear();
  x_y_map.clear();
  for (int ip = 0; ip<graphScanData->GetN(); ip++) {
    
    graphScanData->GetPoint (ip, x_value, y_value);
    //     std::cout << " x_value = " << x_value << std::endl;
    if (std::find(x_std.begin(), x_std.end(), x_value) != x_std.end()) {
      graphScanData->RemovePoint(ip);
      ip--;
    }
    else {
      x_std.push_back(x_value);
      x_y_map[x_value] = y_value;
    }
  }
  
  graphScanData->Set(0);
  
  float data_min_x = -100;
  //---- fix the 0 of the likelihood scan
  minimum = 1000;
  for (std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
    if ( it->second < minimum ) {
      minimum = it->second;
      data_min_x = it->first;
    }
  }
  for (std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
    it->second =  it->second - minimum;
  }
  //---- (end) fix the 0 of the likelihood scan
  
  
  ip = 0;
  for (std::map<double, double>::iterator it = x_y_map.begin(); it != x_y_map.end(); it++) {
    graphScanData->SetPoint( ip, it->first , it->second);
    ip++;
  }
  
  
  
  //---- plot ----
  
  graphScan->GetXaxis()->SetTitle(variable.c_str());
  graphScan->GetYaxis()->SetTitle("-2 #Delta LL");
  
  graphScan  ->Draw("al");
  //   graphScan  ->Draw("aPl");
  
  if (graphScanData) {
    graphScanData->Draw("l");
  }
  
  tex->Draw("same");
  tex2->Draw("same");
  tex3->Draw("same");
  
  
  //  2deltaLogL = 1.00
  //  2deltaLogL = 3.84
  
  //   TLine *line1 = new TLine((limit->GetV2())[0],1.0,(limit->GetV2())[n-1],1.0);
  TLine *line1 = new TLine(minX,1.0,maxX,1.0);
  line1->SetLineWidth(2);
  line1->SetLineStyle(2);
  line1->SetLineColor(kRed);
  line1->Draw(); 
  
  //   TLine *line2 = new TLine((limit->GetV2())[0],3.84,(limit->GetV2())[n-1],3.84);
  TLine *line2 = new TLine(minX,3.84,maxX,3.84);
  line2->SetLineWidth(2);
  line2->SetLineStyle(2);
  line2->SetLineColor(kRed);
  line2->Draw();
  
  TLegend* leg = new TLegend(0.1,0.7,0.48,0.9);
  leg->AddEntry(graphScan,"Expected","l");
  if (graphScanData) {
    leg->AddEntry(graphScanData,"Observed","l");
  }
  
  //   leg->AddEntry(graphScan,"Old","l");
  //   if (graphScanData) {
  //     leg->AddEntry(graphScanData,"New","l");
  //   }
  
  //   leg->AddEntry(graphScan,"Obs 2015 alone","l");
  //   if (graphScanData) {
  //     leg->AddEntry(graphScanData,"Obs 2015 with CR 2016","l");
  //   }
  
  //   leg->AddEntry(graphScan,"Obs 2016 alone","l");
  //   if (graphScanData) {
  //     leg->AddEntry(graphScanData,"Obs 2016 with CR 2015","l");
  //   }
  //   
  
  
  leg->SetFillColor(0);
  leg->Draw();
  
  
  std::cout << " data at minimum:   " << data_min_x << std::endl;
  std::cout << " MC   at minimum:   " <<   mc_min_x << std::endl;
  
  
  //   std::cout << " data at 0:   " << graphScanData->Eval(0) << std::endl;
  //   std::cout << " MC   at 0:   " << graphScan    ->Eval(0) << std::endl;
  
  //   std::cout << " significance data at 0:   " << sqrt(graphScanData->Eval(0)) << std::endl;
  //   std::cout << " significance MC   at 0:   " << sqrt(graphScan    ->Eval(0)) << std::endl;
  
  
  cc->SaveAs("ll.png");

  vector <float> sigma1_x = getLSintersections(graphScan,1.0);
  vector <float> sigma2_x = getLSintersections(graphScan,3.84);
  
  ofstream outfile;
  outfile.open("results.csv",ios_base::app);

  cout << endl << "intersections:" << endl ;
  cout << "1 sigma: ( " << sigma1_x[0] << " ; " << sigma1_x[1] << " )" << endl ;
  cout << "2 sigma: ( " << sigma2_x[0] << " ; " << sigma2_x[1] << " )" << endl ;

  outfile << variable << "," << var_name << ","  ;
  outfile << sigma1_x[0] << "," << sigma1_x[1] << ","  << sigma2_x[0] << "," << sigma2_x[1] << "\n" ; 

  outfile.close();
}