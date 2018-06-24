// ============= プロダクトモーダル ==========================

/**
 * 素のJavascriptによるプロダクトモーダルメニュー展開処理
 *
 * @returns
 */
const modalTriggers = document.getElementsByClassName("js_product-open");
for (modalTrigger of modalTriggers) {
  modalTrigger.addEventListener("click", function () {
    const productModal = document.getElementsByClassName("product_modal")[0];

    productModal.style.height = document.body.clientHeight + "px";
    productModal.classList.add("product_modal--open");

    productUrl = this.getAttribute("href");
    productImg = this.firstElementChild.firstElementChild.getAttribute("src");
    document.getElementById("undergo-anchor").setAttribute("href", productUrl);
    document.getElementById("product-modal-img").setAttribute("src", productImg);

    event.preventDefault();
  }, false);
}

/**
 * 素のJavascriptによるプロダクトモーダルメニュー消去処理
 * プロダクトモーダル領域外をタップすることで、メニューを消去する
 *
 * @returns
 */
document.getElementById("js-product_modal").addEventListener("click", function () {
  const productModal = document.getElementsByClassName("product_modal")[0];
  productModal.classList.remove("product_modal--open");
});

/**
 * プロダクトモーダル領域内をタップされたときの、バブリング停止処理
 *
 * @param event
 * @returns
 */
document.getElementById("js-product-contents_modal").addEventListener("click", function (event) {
  event.stopPropagation();
});


// ============= エラーモーダル ==========================

/**
 * 素のJavascriptによるエラーモーダルメニュー表示処理
 * 他のバリデーションなどから呼び出される想定なので関数定義
 *
 */
var errorModalOpen = function (errorMessage) {
  const modalTriggers = document.getElementsByClassName("js_error-open");
  const errorModal = document.getElementsByClassName("error_modal")[0];

  errorModal.style.height = document.body.clientHeight + "px";
  errorModal.classList.add("error_modal--open");

  document.getElementById("error-message").innerHTML = errorMessage;
  
  return false;
};

if (document.getElementById("error-message").innerHTML) {
  errorModalOpen(document.getElementById("error-message").innerHTML);
}

/**
 * 素のJavascriptによるエラーモーダルメニュー消去処理
 * エラーモーダル領域外をタップすることで、メニューを消去する
 *
 * @returns
 */
document.getElementById("js-error_modal").addEventListener("click", function () {
  const errorModal = document.getElementsByClassName("error_modal")[0];
  errorModal.classList.remove("error_modal--open");
});

/**
 * エラーモーダル領域内をタップされたときの、バブリング停止処理
 *
 * @param event
 * @returns
 */
document.getElementById("js-error-contents_modal").addEventListener("click", function (event) {
  event.stopPropagation();
});