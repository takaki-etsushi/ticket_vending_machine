# タイトル：CUI券売機シミュレータ

## プラットフォーム：
動作環境：PC
* 開発言語： Python
* 開発環境： VScode
* テスト環境： unittest

## 開発担当：
* プロジェクトリーダー：髙木
* WBS、依存関係図：福士
* クラス図、シーケンス図：向口
* プログラム：向口、細田、福士、髙木
* テスト：向口

## 概要：

### ユーザー
* Enterキー押下で画面がクリアされて処理が進む（qキー押下でシミュレータ終了）
* 購入する商品番号押下で商品選択する。指定された番号以外を押した場合は再度入力を促す
* cキー押下で支払いに進む
* 金額を入力しお釣りがあれば返す。金額が不足していれば再度入力を促す
* Enterキー押下でタイトル画面の表示に戻る（qキー押下でシミュレータ終了）
### 管理者
* 最初の画面でescキー押下で管理者画面に進む
* 管理者メニュー1を選択で売上をリセットする
* 管理者メニュー2を選択で商品の価格を変更する（売上がリセットされている場合のみ）
* 管理者メニュー3を選択で管理者画面を終了する
