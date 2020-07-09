# 総務省データ取得プログラム
総務省の統計データ（e-Stat）のデータを取得するgasプログラム格納場所

## 各プログラム
### `getSimpleStatsList.gs`
`e-stat`でデータを取得する際には`statsDataId`が必要になるため、
このGASによってレポート別の`statsDataId`を調査する。

### `getSimpleStatsData.gs`
`statsDataId`を利用して総務省の統計データを取得し、
spread sheetにデータを反映する

## 参照リンク
- https://www.e-stat.go.jp/stat-search/database?page=1
