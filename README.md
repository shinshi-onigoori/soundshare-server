# outup-backend

これがoutupのバックエンドです！

# 開発規約
## 開発を始めるには？
- $ git　checkout -b {issue-name}/#{issue-number}
- 上記コマンドでブランチを切ること
## アーキテクチャについて
- entity
- repository
- service
の3層のアーキテクチャを採用
### entityとは？
データモデルの項目を定義したクラス
### repositoryとは？
データの永続化を責務として持つクラスを集めたレイヤー<br>
後々RDBを使うことになった際にもこのレイヤーからアクセスする
### serviceとは？
repositoryレイヤのロジックを手続き的に組み合わせてAPIとしての機能を提供するレイヤー

# デプロイについて
outupのバックエンドは Google App Engine上で動いています。
そのため、srcディレクトリに移動して
```
$ gcloud app deploy
```
のコマンドを使用してデプロイします。
(タイムアウトしたときは -> $ gcloud config set app/cloud_build_timeout 1200)

## cloudbuid config を使用したdeploy
```
gcloud builds submit --config cloudbuild.yml
```

## 依存関係に修正がある時
```
$ cd src
$ pip freeze > requirements.txt
```
上記コマンドを使用してsrcフォルダ内のrequirements.txtにパッケージ情報を更新すること

# ローカルでの実行方法
```
$ cd src
$ python main.py
```