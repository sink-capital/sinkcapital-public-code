function myFunction() {
  // アクセス先
  var url = "https://api.e-stat.go.jp/rest/3.0/app/getSimpleStatsList?appId=__YOUR_APP_ID__"
  // POSTリクエスト
  var response = UrlFetchApp.fetch(url);
  // HTML結果を取得
  var csvText = response.getContentText("UTF-8");
  var values = Utilities.parseCsv(csvText);
  SpreadsheetApp.getActiveSheet().getRange(1, 1, values.length, values[0].length).setValues(values);
}
