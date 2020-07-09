function myFunction() {
  var startRow = 1;
  var values = getApiData("0003102823");
  SpreadsheetApp.getActiveSpreadsheet().getSheetByName('result').getRange(startRow, 1, values.length, values[0].length).setValues(values);
}

function getApiData(statsDataId) {
  var appId = "__YOUR_APP_ID__";
  var url = "https://api.e-stat.go.jp/rest/3.0/app/getSimpleStatsData?appId=" + appId + "&statsDataId=" + statsDataId + "&cntGetFlg=N&metaGetFlg=N?explanationGetFlg=N&annotationGetFlg=N";
  // POSTリクエスト
  var response = UrlFetchApp.fetch(url);
  // HTML結果を取得
  var csvText = response.getContentText("UTF-8");
  var values = Utilities.parseCsv(csvText);
  // メタ情報を除く
  return values.slice(28)
}
