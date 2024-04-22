const questions = [
    {
        // Question 1
        question: "Which is the largest animal in the world?",
        answers: [
            { text: "Shark", correct: false },
            { text: "Blue Whale", correct: true },
            { text: "Elephant", correct: false },
            { text: "Giraffe", correct: false },
        ]
    },
    {
        // Question 2
        question: "Who was the founder of Pakistan?",
        answers: [
            { text: "Modhi", correct: false },
            { text: "Mian Sahab", correct: false },
            { text: "Khan Sahab", correct: false },
            { text: "Donald Trump", correct: false },
            { text: "Muhammad Ali Jinnah", correct: true },
        ]
    },
    {
        // Question 3
        question: "Which is the smallest continent in the world?",
        answers: [
            { text: "Asia", correct: false },
            { text: "Australia", correct: true },
            { text: "Arctic", correct: false },
            { text: "Africa", correct: false },
        ]
    },
    {
        // Question 4
        question: "Which is the largest desert in the world?",
        answers: [
            { text: "Kalahari", correct: false },
            { text: "Gobi", correct: false },
            { text: "Sahara", correct: false },
            { text: "Antarctica", correct: true },
        ]
    },
    {
        // Question 5
        question: "Which is the smallest country in the world?",
        answers: [
            { text: "Lahore", correct: false },
            { text: "Nepal", correct: false },
            { text: "Vatican City", correct: true },
            { text: "Paris", correct: false },
        ]
    }
]

const questionElement = document.getElementById("question");
const answersContainer = document.getElementById("answer_buttons");
const next_btn = document.getElementById("next_button");

let currentQuestionIndex = 0;
let score = 0;


function startQuiz () {
    currentQuestionIndex = 0;
    score = 0;
    next_btn.innerText = "Next";

    showQuestion();
}


const showQuestion = () => {
    resetState();
    let currentQuestion = questions[currentQuestionIndex];
    let questionNo = currentQuestionIndex + 1;
    // questionElement.innerText = `${questionNo}. ${currentQuestion.question}`;
    questionElement.innerText = questionNo + ". " + currentQuestion.question;

    currentQuestion.answers.forEach((answer) => {
        const button = document.createElement("button");
        button.innerText = answer.text;
        button.classList.add("btn");

        if(answer.correct) {
            button.dataset.correct = answer.correct;
        }

        button.addEventListener("click", selectAnswer);

        answersContainer.append(button);
    });


}

function selectAnswer (event) {
    const selectedBtn = event.target;

    const isCorrect = selectedBtn.dataset.correct;

    if(isCorrect == "true") {
        score++;
        selectedBtn.classList.add("correct");
    }
    else {
        score--;
        selectedBtn.classList.add("incorrect");
    }

    // console.log(answersContainer.children);
    let buttonAray = Array.from(answersContainer.children);

    buttonAray.forEach((button) => {
        if(button.dataset.correct == "true") {

            button.classList.add("correct");
        }
        button.disabled = true;
    })

    next_btn.style.display = "block";
    let questionNo = currentQuestionIndex + 1;
    next_btn.innerHTML = `Next <br> ${questionNo} out of ${questions.length}`;
}

function resetState () {
    next_btn.style.display = "none";

    while(answersContainer.firstChild) {
        answersContainer.removeChild(answersContainer.firstChild);
    }
}

const showScore = () => {
    resetState();
    questionElement.innerText = `You scored ${score} out of ${questions.length}`

    next_btn.style.display = "block";
    next_btn.innerText = "Play Again";
}

function handleNextQuestion () {
    currentQuestionIndex++;

    if (currentQuestionIndex < questions.length) {
        showQuestion();
    }
    else {
        showScore();
    }
}

next_btn.addEventListener("click", () => {
    if(currentQuestionIndex < questions.length) {
        handleNextQuestion();
    }
    else {
        startQuiz();
    }
})


// Start the Quiz
startQuiz();