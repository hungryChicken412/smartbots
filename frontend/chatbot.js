

function send(x){

    try {
        ws.send(x);
    } catch (error) {
        console.log(error);
    }
    console.log("Msg sent ", x);
}





const popup = document.querySelector('.smartbot-chat-popup');
const chatBtn = document.querySelector('.smartbot-chat-btn');
const submitBtn = document.querySelector('.smartbot-submit');
const chatArea = document.querySelector('.smartbot-chat-area');
const inputElm = document.querySelector('input');
const infopanel = document.querySelector('.smartbot-information-panel')

const endconvo = document.querySelector('#end-convo');
const startconvo = document.querySelector('#start-convo')
const startwait = document.querySelector('#established')

var startedConvo = false;
//   chat button toggler 

chatBtn.addEventListener('click', ()=>{
    popup.classList.toggle('show');
    if (!startedConvo){
        startedConvo = true;
        startConversation()
    }
})

function startConversation(){
    const ws = new WebSocket("ws://127.0.0.1:567/20e7587ec47237ab823c");
    console.log(ws);
    window.ws = ws;

    ws.onmessage = function(event){
        try {
            startwait.remove()
        } catch{
            
        }
        if (event.data == "Something Went Wrong! Please Contact Support"){
            endconversation()

        }
        showMessage(event.data)
    };

    chatArea.scrollTop = chatArea.scrollHeight;
}

function showMessage(message){
    let divided = message.split("<DIVIDER>")
    
    let temp = `
    <div class="smartbot-income-msg smartbot-msg-card">
        <span class="smartbot-msg">${divided[0]}</span>
    </div>`;

    if (divided.length > 1){
        let options = divided[1].split("<OPTION>")
        options.forEach(opt => {
            temp += `
            <div class="smartbot-income-msg smartbot-msg-card smartbot-choice-msg"  onclick="choose('${opt}')">
                <span class="smartbot-msg">${opt}</span>
            </div>`
        });
    }
    

    chatArea.insertAdjacentHTML("beforeend", temp);

    chatArea.scrollTop = chatArea.scrollHeight;
}


function endconversation(){
    showMessage('[CONVERSATION ENDED]')
    endconvo.remove()
    inputElm.disabled = true;
    submitBtn.disabled = true;
    
    window.ws.close(1000);
    
    let startconvohtml = `[Conversation Ended]`;
    infopanel.insertAdjacentHTML("beforeend", startconvohtml)
}


function choose(n){
    sendMsg(n)

}

// send msg 
function sendMsg(data = null){
    let userInput = inputElm.value;
    if (data != null){
        userInput = data;
    }

    let temp = `<div class="smartbot-my-msg">
    <span class="smartbot-usr-msg">${userInput}</span>
    </div>`;

    chatArea.insertAdjacentHTML("beforeend", temp);
    chatArea.scrollTop = chatArea.scrollHeight;

    send(userInput);
    

    inputElm.value = '';

}
submitBtn.addEventListener('click', (e) => {
    sendMsg()
})
endconvo.addEventListener('click', (e) => {
    endconversation();
    
})

inputElm.addEventListener('keypress', function (e) {
    if (e.key=="Enter"){
        sendMsg()
    }
});