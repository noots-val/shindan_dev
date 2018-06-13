/**
 * 素のJavascriptによるモーダルメニュー展開処理
 *
 * @returns
 */
const modalTriggers =  document.getElementsByClassName("js_product-open");

for(modalTrigger of modalTriggers){
  modalTrigger.addEventListener("click", function() {
    const productModal = document.getElementsByClassName("product_modal")[0];
    productModal.style.height = document.body.clientHeight + "px";
    productModal.classList.add("product_modal--open");

    productUrl = this.getAttribute("href");
    productImg = this.firstElementChild.firstElementChild.getAttribute("src");

    document.getElementById("undergo-anchor").setAttribute("href", productUrl)
    document.getElementById("product-modal-img").setAttribute("src", productImg)
    event.preventDefault();
  }, false );
}

/**
 * 素のJavascriptによるモーダルメニュー消去処理
 * モーダル領域外をタップすることで、メニューを消去する
 *
 * @returns
 */
document.getElementById("js-product_modal").addEventListener("click", function() {
  const productModal = document.getElementsByClassName("product_modal")[0];
  productModal.classList.remove("product_modal--open");
});


/**
 * モーダル領域内をタップされたときの、バブリング停止処理
 *
 * @param event
 * @returns
 */
document.getElementById("js-product-contents_modal").addEventListener("click", function(event) {

	event.stopPropagation()
});