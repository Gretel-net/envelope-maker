# 封筒作るん

JSON テンプレートから封筒に宛名とかの PDF 作るやつ

## Usage

```shell
./main.py -t [TEMPLATE_PATH] -p [LAYOUT_PATH] -o [OUTPUT] --a4
```

```shell
# Using Docker
docker build -t envelope-maker .
docker run \
-v $PWD/dist:/var/dist \
-v $PWD/layout:/var/envelope-maker/layout \
-v $PWD/template:/var/envelope-maker/template \
envelope-maker \
./main.py -t ./template/template.json -p ./layout/naga_3go.json -o /var/dist/sample.pdf --a4
```

`-t`: 宛先 JSON
`-p`: 封筒レイアウト JSON
`-o`: 出力先
`--a4` A4 互換モード(option)

宛名のサンプル: template.json
長形 3 号のサンプル: naga_3go.json

サイズ･位置パラメータは `mm` ミリメートル単位

## 上手く動かなかったらすまん

うちのプリンターでしか動かんかもしれん

動作確認済み: ブラザー HL-L2365DW

## サンプル

![A4モード](./docs/sample_pdf_ss_a4.png)
![ネイティブモード](./docs/sample_pdf_ss_native.png)

[印刷結果](./docs/print_sample.pdf)

## ＩＰＡフォント

ＩＰＡフォントをバンドルしてるよ

[IPA_Font_License_Agreement_v1.0.txt](./fonts/IPA_Font_License_Agreement_v1.0.txt) 読んでね
