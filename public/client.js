window.onload = function() {
	let score = 0;
	let wordToSpell;
	let spelling = [];
	let speechResult = '';
	const socket = io.connect('https://localhost:3000');
	socket.on('spell', function(word) {
		console.log('Spell the word', word);
		wordToSpell = word;
	});

	window.SpeechRecognition =
		window.webkitSpeechRecognition || window.SpeechRecognition;
	const recognition = new SpeechRecognition();
	recognition.lang = 'en-ZA';
	recognition.interimResults = false;
	recognition.continuous = true;
	recognition.interimResults = true;

	recognition.onresult = event => {
		console.log('result');
		const speechToText = event.results[0][0].transcript;
		console.log(speechToText);
		speechResult = speechToText;
	};

	document.addEventListener('mousedown', () => {
		recognition.start();

		console.log('mousedown');
	});

	document.addEventListener('mouseup', () => {
		recognition.stop();
		const spellingResultData = { word: wordToSpell, spelling: speechResult };
		checkSpelling(wordToSpell, speechResult);
		socket.emit('nextWord', spellingResultData);
		console.log(spellingResultData);
	});

	function checkSpelling(word, spelling) {
		const spellingWithoutWhiteSpace = spelling.replace(/\s/g, '');
		if (word === spellingWithoutWhiteSpace) {
			score += 100;
			console.log(score);
		} else {
			console.log('not quite right :|');
		}
	}
};
