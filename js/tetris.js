import BLOCKS from "./blocks.js";

// DOM

const playground = document.querySelector(".playground > ul");
const gameText = document.querySelector(".game-text")
const scoreDisplay = document.querySelector(".score")
const resartbutton = document.querySelector(".game-text > button")
//Setting

const GAME_ROWS=20;
const GAME_COLS=10;

// variables

let score = 0;
let duration = 500;
let downInterval;
let tempmovingItem;
let movingitem={
    type:"" ,
    direction :0,
    top: 0,
    left: 3,
};



// functions
init();

function init(){
    
    tempmovingItem = {...movingitem};

    for (let i =0; i <GAME_ROWS; i++){
        prependNewline()
        
    }
    generateNesbolck()
}


function prependNewline(){
    const li=document.createElement("li");
    const ul=document.createElement("ul");
    for (let j=0; j<GAME_COLS; j++){
        const matrix=document.createElement("li");
        ul.prepend(matrix);
    }
    li.prepend(ul);
    playground.prepend(li);
}

function renderBlocks(moveType=""){
    const {type, direction, top, left} = tempmovingItem;
    const movingBlocks = document.querySelectorAll(".moving");
    movingBlocks.forEach(moving => {
        moving.classList.remove(type,"moving");        
    });

    BLOCKS[type][direction].some(block=>{
        const x = block[0]+left;
        const y = block[1]+top;
        

        // 변수 xxx= 조건 ? 참일경우: 거짓일 경우
        const target = playground.childNodes[y] ? playground.childNodes[y].childNodes[0].childNodes[x] : null;
        console.log(target)
        const isAvailable = checkEmpty(target);

        if(isAvailable){
            target.classList.add(type,"moving");
        } else{
            tempmovingItem={...movingitem};
            if (moveType==="retry"){
                clearInterval(downInterval);
                showGameoverText();
            }
            setTimeout(()=>{
                renderBlocks("retry");
                if(moveType==="top"){
                    seizeBlock();
                }
                
            },0)
            //renderBlocks();
            return true;
        }
        });
        
        movingitem.left=left;
        movingitem.top=top;
        movingitem.direction=direction;
        

    
   
}
function showGameoverText(){
    gameText.style.display ="flex"

}

function seizeBlock(){

    const movingBlocks = document.querySelectorAll(".moving");
    movingBlocks.forEach(moving => {
        moving.classList.remove("moving");
        moving.classList.add("seized");
    });
    checkMatch()
}

function checkMatch(){
    const childNodes = playground.childNodes;
    childNodes.forEach(child=>{
        let matched =true;
        child.children[0].childNodes.forEach(li=>{
            if(!li.classList.contains("seized")){
                matched =false;
            }
        })
        if(matched){
            child.remove();
            prependNewline();
            score++;
            scoreDisplay.innerText=score;

        }
    })

    generateNesbolck();


}

function generateNesbolck(){

    clearInterval(downInterval);
    downInterval=setInterval(()=>{
        moveBlock("top",1);
    },duration);

    const blockArray=Object.entries(BLOCKS);
    const randomIndex=Math.floor(Math.random()*blockArray.length);
    movingitem.type=blockArray[randomIndex][0];
    movingitem.left=3;
    movingitem.top=0;
    movingitem.direction=0;
    tempmovingItem={...movingitem};
    renderBlocks();
}

function checkEmpty(target){
    
    if(!target || target.classList.contains("seized")) {
        return false;
    }
    return true;
}

function moveBlock(moveType, amount){
    tempmovingItem[moveType] += amount;
    renderBlocks(moveType)
}

function changedirection(){
    const direction = tempmovingItem.direction;
    direction===3 ? tempmovingItem.direction =0 : tempmovingItem.direction+=1;

    renderBlocks()
}

function dropBlock(){
    clearInterval(downInterval);
    downInterval=setInterval(()=>{
        moveBlock("top",1)
    },10)
}

// event handling
document.addEventListener("keydown",e=>{
    switch(e.keyCode){
        case 39:
            moveBlock("left",1);
            break;
        case 37:
            moveBlock("left",-1);
            break;
        case 40:
            moveBlock("top",1);
            break;
        case 38:
            changedirection();
            break;
        case 32:
            dropBlock();
            break;
        default:
            break;
    }
    //console.log(e)
})

resartbutton.addEventListener("click", () => {
    playground.innerHTML = "";
    gameText.style.display="none"
    init();
})