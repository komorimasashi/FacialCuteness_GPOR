# 研究論文
「Examination of morphological traits of children's faces related to perceptions of cuteness using Gaussian process ordinal regression. Frontiers in Psychology」

Komori, M., Teraji, T., Shiroshita, K., & Nittono, H. (2022). Frontiers in Psychology, 13.

# ファイル内容
```
.
├── 002.psyexp
├── 002_lastrun.py  かわいいの実験システム(psychopyで作成)
├── README.md
├── data            探索点に対応した応答データ
├── ego
│   ├── gpor.py    事後分析での関数 (GPOR使用)
│   └── stimulation
|        └──fece.py -1〜1のランダム点の関数（実験で使用）
|
├── image_data      幼児の顔を合成した刺激画像
├── koushinchu.png  試行の間のグレー画像
└── post_process    応答データで事後分析
```
# 実行手順
## 環境の構築
GPfrowを使っているためCUDA11以上のtensorflow2系が必要です．
まずパッケージのインストール
```
pip install -r requirements.txt
```

1. かわいいの評価実験
```
python 002_lastrun.py 
```
で実験がスタート
実験をスタートするとdataフォルダが生成され，そこに実験データが保存される．
ここで必要になるファイルは，filename_result.csvとfilename_response.csv

2. 事後分析（効用関数の推定）
dataファイルのfilename_result.csvとfilename_response.csvを使ってGPORで個人の効用関数を推定する.

```
python ./post_process/post_process_prottype.py
```
個々人の予測平均filename_mu_result.csvと予測分散がfilename_var_result.csvが保存される．
全体の予測平均はmu_z.csv,予測分散はsig_2_mu.csvで保存される






