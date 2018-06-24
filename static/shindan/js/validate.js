// ============= 質問フォーム ==========================

/**
 * 全てのラジオボタンがチェックされていることを検査
 *
 * @returns
 */
var validateQuestionForm = function() {
  const questionCount = document.getElementsByClassName("question-sentence_dm").length;
  const radios = document.getElementsByClassName("radio-input_form");
  
  let checkRadioCount = 0;
  for (var radio of radios) {
    if (radio.checked == true) checkRadioCount++;
  }

  if (questionCount != checkRadioCount) {
    return errorModalOpen("質問は全て回答必須です。");
  }
};