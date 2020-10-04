console.log("Chrome extension go?");



window.addEventListener('mouseup',wordSelected);

function wordSelected(){
  console.log('word selected');
  let selectedText = window.getSelection().toString().trim();
  console.log(selectedText);
  if (selectedText.length>0){
    let message = {
      text:selectedText
    }
    chrome.runtime.sendMessage(message)
  }
  else{
    console.log("text not selected")
  }
}



