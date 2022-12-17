# Article Info
Citation: Komori M, Teraji T, Shiroshita K and Nittono H (2022) Examination of morphological traits of children's faces related to perceptions of cuteness using Gaussian process ordinal regression. Front. Psychol. 13:979341. doi: 10.3389/fpsyg.2022.979341

https://doi.org/10.3389/fpsyg.2022.979341

Abstract: Konrad Lorenz, an ethologist, proposed that certain physical elements are perceived as cute and induce caretaking behavior in other individuals, with the evolutionary function of enhancing offspring survival. He called these features Kindchenschema, baby schema. According to his introspection, these include a large forehead, chubby round features, and chubby cheeks. Previous studies are limited to examining the effects of these facial features on perceived cuteness. However, other morphological factors may be related to perceived cuteness. This study uses Bayesian optimization, one of the global sequential optimization methods for estimating unknown functions, to search for facial morphological features that enhance the perceptions of facial cuteness. We applied Bayesian optimization incorporating Gaussian process ordinal regression (GPOR), which allows an estimation of the latent cuteness function based on evaluations using the Likert scale. A total of 96 preschool children provided the facial images used in this study. We summarized the facial shape variations using methodologies of geometric morphometrics and principal component analysis (PCA) up to the third principal component (PC), which we refer to as the face space. A total of 40 participants evaluated the images created by warping the average facial texture of the children's faces with randomly generated parameters in the face space. Facial traits related to perceived cuteness were estimated based on the averaged cuteness function. Perceived cuteness was linked to the relative lower position of facial components and narrower jawline but not to the forehead height.

Received: 15 July 2022; Accepted: 17 October 2022;
Published: 03 November 2022.

# ファイル内容
```
.
├── 002.psyexp
├── 002_lastrun.py      かわいいの実験システム(psychopyで作成)
├── README.md
├── data                探索点に対応した応答データ
├── ego
│   ├── gpor.py         事後分析での関数 (GPOR使用)
│   └── stimulation
|        └──fece.py     -1〜1のランダム点の関数（実験で使用）
|
├── image_data          幼児の顔を合成した刺激画像
├── koushinchu.png      試行の間のグレー画像
├── requirements.txt    必要なパッケージ 
└── post_process        応答データで事後分析
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






