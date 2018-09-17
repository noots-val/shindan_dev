// cookieデータの取得
function getCookie(cookieName) {
  let result;

  // 目的となるcookieがValueに含まれている場合にもcookieNameだけを取得するため'='を付ける
  const indexOfName = cookieName + '=';
  let AllCookie = document.cookie;

  // 目的となるcookieNameが含まれているかを判別→何文字目から何文字目までかを算出し、取得
  let position = AllCookie.indexOf(indexOfName);
  if (position != -1) {
    const startIndex = position + indexOfName.length;
    let endIndex = AllCookie.indexOf(';', startIndex);

    if (endIndex == -1) endIndex = AllCookie.length;

    result = decodeURIComponent(
      AllCookie.substring(startIndex, endIndex));
  }

  return result;
}


// レーダーチャートの作成
const peacockeryType = decodeURI(getCookie('PEACOCKERY_TYPE'));
const loyaltiesType = decodeURI(getCookie('LOYALTIES_TYPE'));
const admissibilityType = decodeURI(getCookie('ADMISSIBILITY_TYPE'));
const responsibilityType = decodeURI(getCookie('RESPONSIBILITY_TYPE'));
const cooperativenessType = decodeURI(getCookie('COOPERATIVENESS_TYPE'));
const peacockeryPoint = getCookie('PEACOCKERY_POINT');
const loyaltiesPoint = getCookie('LOYALTIES_POINT');
const admissibilityPoint = getCookie('ADMISSIBILITY_POINT');
const responsibilityPoint = getCookie('RESPONSIBILITY_POINT');
const cooperativenessPoint = getCookie('COOPERATIVENESS_POINT');
const ctx = document.getElementById('chart').getContext('2d');
const myChart = new Chart(ctx, {
  type: 'radar',
  options: {
    legend: { //凡例の削除
      display: false
    },
    scale: {
      pointLabels: { //軸ラベルの設定
        fontSize: 15
      },
      ticks: { //軸目盛の設定
        stepSize: 5,
        max: 25,
        fontSize: 15,
        beginAtZero: true
      }
    }
  },


  data: {
    labels: [peacockeryType, loyaltiesType, admissibilityType, responsibilityType, cooperativenessType],
    datasets: [{
      data: [peacockeryPoint, loyaltiesPoint, admissibilityPoint, responsibilityPoint, cooperativenessPoint],
      backgroundColor: "rgba(78,229,218,0.4)",
      borderColor: "rgba(78,229,218,0)",
      pointRadius: 0,
    }]
  }
});