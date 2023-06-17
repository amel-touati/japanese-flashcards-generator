const translation = document.querySelector('.translation');
console.log(translation);

const meanings = document.querySelectorAll('.meaning h5');
console.log(meanings);

for (i = 0; i < meanings.length; i++) {
    if (translation.innerHTML.includes('meet')) {
        const text = meanings[i].innerHTML
        console.log(text)
    }
}

// function to color the word in translation that is in kanji meaning

for (let i = 0; i < meanings.length; i++) {
    if (translation.innerHTML.includes(meanings[i].innerHTML)) {
        // translation.style.color = 'red';
        const word = meanings[i].innerHTML;
        const coloredWord = `<span style="color: #5E8AB1;">${meanings[i].innerHTML}</span>`;
        const coloredSentence = translation.textContent.replace(word, coloredWord);
        translation.innerHTML = coloredSentence;
        console.log(translation);
        break;
    }
}

// coloring the kanji in sentence that is is the same as kanji in question
const kanji = document.querySelector('.kanji');
console.log(kanji);

const sentence = document.querySelectorAll('.sentence');
console.log(sentence);


for (let i = 0; i < sentence.length; i++) {
    if (sentence[i].innerHTML.includes(kanji.innerHTML)) {
        // translation.style.color = 'red';
        const word = kanji.innerHTML;
        const coloredWord = `<span style="color: #5E8AB1;">${word}</span>`;
        const coloredSentence = sentence[i].textContent.replace(word, coloredWord);
        sentence[i].innerHTML = coloredSentence;
        console.log(sentence[i]);
        break;
    }
}

//coloring the hiragana after . in kun readings
const b = false
const coloredSentences = [];
let k;
const kun_readings = document.querySelector('.kun');
console.log(kun_readings);

const kun_readings_text = kun_readings.innerHTML;
const kun_readings_split = kun_readings_text.split('、')

for (let i = 0; i < kun_readings_split.length; i++) {
    const kun_word = kun_readings_split[i];
    let k;

    for (let j = 0; j < kun_word.length; j++) {
        if (kun_word[j] == '.') {
            k = j;
            break;
        }
    }

    if (typeof k !== 'undefined') {
        const word = kun_word.substring(k + 1);
        const coloredWord = `<span style="color: #00B0FF;">${word}</span>`;
        const coloredSentence = kun_word.replace(word, coloredWord);
        coloredSentences.push(coloredSentence)

        console.log(coloredSentence)
    } else {
        coloredSentences.push(kun_word)
    }
    kun_readings.innerHTML = coloredSentences;
    kun_readings.innerHTML = kun_readings.innerHTML.replace(/,/g, '、');
    kun_readings.innerHTML = kun_readings.innerHTML.replace(/\./g, '');

}

var sentenceDiv = document.querySelector('.sentence');
var translationDiv = document.querySelector('.translation');
var meaningDiv = document.querySelector('.meaning');
var h5Elements = meaningDiv.querySelectorAll('h5');

function adjustFontSize() {
    var sentenceOverflow = sentenceDiv.scrollWidth > sentenceDiv.clientWidth;
    var translationOverflow = translationDiv.scrollWidth > translationDiv.clientWidth;
    var meaningOverflow = meaningDiv.scrollWidth > meaningDiv.clientWidth;

    if (sentenceOverflow) {
        sentenceDiv.style.fontSize = '10px'; // Adjust the font size as needed
    } else {
        sentenceDiv.style.fontSize = 'inherit'; // Reset the font size
    }

    if (translationOverflow) {
        translationDiv.style.fontSize = '10px'; // Adjust the font size as needed
    } else {
        translationDiv.style.fontSize = 'inherit'; // Reset the font size
    }

    if (meaningOverflow) {
        h5Elements.forEach(function(h5) {
            h5.style.fontSize = '10px'; // Adjust the font size as needed
        });
    } else {
        h5Elements.forEach(function(h5) {
            h5.style.fontSize = 'inherit'; // Reset the font size
        });
    }
}

// Call the adjustFontSize function whenever the window is resized
window.addEventListener('resize', adjustFontSize);

// Call the adjustFontSize function initially
adjustFontSize();


function playAudio(audioPath) {
    var audio = new Audio(audioPath);
    audio.onerror = function() {
        console.error('Failed to load audio:', audioPath);
    };
    audio.play();
}