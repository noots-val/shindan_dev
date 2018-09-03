// cookieデータの取得
function GetCookie(cookieName) {
  var result = null;
  var indexOfName = cookieName + '=';
  var AllCookie = document.cookie;

  var position = AllCookie.indexOf(indexOfName);
  if (position != -1) {
    var startIndex = position + indexOfName.length;
    var endIndex = AllCookie.indexOf(';', startIndex);
    if (endIndex == -1) {
      endIndex = AllCookie.length;
    }

    result = decodeURIComponent(
      AllCookie.substring(startIndex, endIndex));
  }

  return result;
}

// レーダーチャートの作成
const peacockeryType = GetCookie('PEACOCKERY_TYPE');
const loyaltiesType = GetCookie('LOYALTIES_TYPE');
const admissibilityType = GetCookie('ADMISSIBILITY_TYPE');
const responsibilityType = GetCookie('RESPONSIBILITY_TYPE');
const cooperativenessType = GetCookie('COOPERATIVENESS_TYPE');
const peacockeryPoint = GetCookie('PEACOCKERY_POINT');
const loyaltiesPoint = GetCookie('LOYALTIES_POINT');
const admissibilityPoint = GetCookie('ADMISSIBILITY_POINT');
const responsibilityPoint = GetCookie('RESPONSIBILITY_POINT');
const cooperativenessPoint = GetCookie('COOPERATIVENESS_POINT');
var ctx = document.getElementById('chart').getContext('2d');
var myChart = new Chart(ctx, {
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