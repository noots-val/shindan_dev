## ディレクトリ構造
1. Foundation
Reset.cssやNormalize.cssなどを用いたブラウザのデフォルトスタイルの初期化や、CSSライブラリなどを配置する。

2. Layout
画面の大枠を構成するBlockを定義する。
CSSファイルはブロックごとに分割する。
その画面独自の定義がある場合は、画面名のディレクトリを作ってそちらに定義する。

3. Object
BEMを定義する。画面を問わずの共通パーツ。（実際に複数回呼ばれるかはどうでもいい）
CSSファイルはブロックごとに分割する。
ProjectとComponentの区別などは行わない。（混乱しやすいので）

4. Utility
LayoutやObjectとすることが不適切な要素を定義する。
CSSファイルは用途ごと（js操作用、アニメーション用など）に分割する。


## 画面構造
1. Block
機能を持った要素の集合。
Blockは互いに影響しあわないが、Block内にBlockを配置することは可能。
ex): ヘッダー、検索フォームなど

2. Element
Blockを構成する、機能を類推出来る最小の要素。
親以外のBlock以外からの影響は絶対に受けてはならない。
ex): ラベル、ボタン、テキストエリアなど

3. Modifier
Block、Elementの一部分を変更し、Objectのバージョン違いを作り出すための修飾。
Block、Elementのどちらかに一つのみ付与を許可。
ex): フォントやカラー、サイズなど



## 使用例
基本的にはMindBEMdingを用いる。
シングルクラス設計だが、Utilityに限りマルチクラスを許可。

<class="sample-block__sample-element--blue js-handler">

※ MindBEMding
BEMの命名規則。
block__element--modifier のように, blockとelementはアンダースコア2つで区切り, elementとmodifierはハイフン2つで区切る。
blockが複数単語になる場合は, 単語と単語の間はハイフン1つで区切る. element, modifierが複数単語になる場合も同様である。
例えばarticle-listというblockの中にarticle-titleというelementがある場合, このelementのクラス名は article-list__article-title となる.


## 規則

### 命名規則
BEM

### ファイル名


### ファイル内構造
下のように、gridレイアウトによる配置とそれ以外の属性では一行を空ける。

.product__image-area {
  grid-column: 1/3;
  grid-row: 2;

  display: flex;
  justify-content: center;
  width: auto;
  height: 200px;
  background-color: #FFFFFF;
}
