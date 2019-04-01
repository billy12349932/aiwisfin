window.onload = function speak(){
	var synth = window.speechSynthesis;
    var utterThis = new SpeechSynthesisUtterance('您好，請問需要什麼服務?');
    utterThis.volume = 1;
	utterThis.pitch = 1;
    utterThis.rate = 1.5;
    utterThis.lang = 'zh';
	synth.speak(utterThis);
};


$('.dropdown-button').dropdown({
    inDuration: 300,
    outDuration: 225,
    constrainWidth: false, // Does not change width of dropdown to that of the activator
    hover: false, // Activate on hover
    gutter: 0, // Spacing from edge
    belowOrigin: false, // Displays dropdown below the button
    alignment: 'left', // Displays dropdown with edge aligned to the left of button
    stopPropagation: false // Stops event propagation
}
);
$(".button-collapse").sideNav();
resize()
window.onresize = resize;
function resize(){
 $('.card.brown.lighten-2').height($( window ).height()-160);
 if ($( window ).width() >=993){
	$('#chatbox').height($( window ).height()-255);
	$('#chatbox_content').height($( window ).height()-255);
	$('.panel-body').height($( window ).height()-275);
 }else {
	$('#chatbox').height($( window ).height()-214);
	$('#chatbox_content').height($( window ).height()-214);
	$('.panel-body').height($( window ).height()-234);
 }
}
var query = ''
var date1 = new Date();
var date2 = new Date();

$( document ).ready(function() {
	if (document.images) {
		var img1 = new Image();
		img1.src = "/img/user.png";
	}

	var synth = window.speechSynthesis;
	var state = 0;

	function speak(inputTxt){
	  if(inputTxt !== ''){
		var utterThis = new SpeechSynthesisUtterance(inputTxt);
		utterThis.pitch = 1;
		utterThis.rate = 1.5;
		synth.speak(utterThis);
	  }
	}

	var request = function(e) {
		state = 0;
		query = $('#input_text').val();
		$('#input_text').val('');
        $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix right"><img src="/img/user.png" alt="User Avatar" class="mfr circle responsive-img" align="right"><p class="right">' + query + '</p></div></li>');
		$(".panel-body").stop().animate({
			scrollTop: $(".panel-body")[0].scrollHeight
		}, 1000);
		function response(){
            if (state == 0) {
				$(".panel-body").stop().animate({
					scrollTop: $(".panel-body")[0].scrollHeight
				}, 1000);}
		}
		setTimeout(response, 1000);
	};

    var request_2 = function (e) {
        state = 0;
        query = $('a#sendbox2').attr("title");
        $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix right"><img src="/img/user.png" alt="User Avatar" class="mfr circle responsive-img" align="right"><p class="right">' + query + '</p></div></li>');
        $(".panel-body").stop().animate({
            scrollTop: $(".panel-body")[0].scrollHeight
        }, 1000);
        function response() {
            if (state == 0) {
                $(".panel-body").stop().animate({
                    scrollTop: $(".panel-body")[0].scrollHeight
                }, 1000);
            }
        }
        setTimeout(response, 1000);
    };
    var request_3 = function (e) {
        state = 0;
        query = $('a#sendbox3').attr("title");
        $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix right"><img src="/img/user.png" alt="User Avatar" class="mfr circle responsive-img" align="right"><p class="right">' + query + '</p></div></li>');
        $(".panel-body").stop().animate({
            scrollTop: $(".panel-body")[0].scrollHeight
        }, 1000);
        function response() {
            if (state == 0) {
                $(".panel-body").stop().animate({
                    scrollTop: $(".panel-body")[0].scrollHeight
                }, 1000);
            }
        }
        setTimeout(response, 1000);
    };
    var request_4 = function (e) {
        state = 0;
        query = $('a#sendbox4').text();
        $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix right"><img src="/img/user.png" alt="User Avatar" class="mfr circle responsive-img" align="right"><p class="right">' + query + '</p></div></li>');
        $(".panel-body").stop().animate({
            scrollTop: $(".panel-body")[0].scrollHeight
        }, 1000);
        function response() {
            if (state == 0) {
                $(".panel-body").stop().animate({
                    scrollTop: $(".panel-body")[0].scrollHeight
                }, 1000);
            }
        }
        setTimeout(response, 1000);
    };
    var request_5 = function (e) {
        state = 0;
        query = $('a#sendbox5').text();
        $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix right"><img src="/img/user.png" alt="User Avatar" class="mfr circle responsive-img" align="right"><p class="right">' + query + '</p></div></li>');
        $(".panel-body").stop().animate({
            scrollTop: $(".panel-body")[0].scrollHeight
        }, 1000);
        function response() {
            if (state == 0) {
                $(".panel-body").stop().animate({
                    scrollTop: $(".panel-body")[0].scrollHeight
                }, 1000);
            }
        }
        setTimeout(response, 1000);
    };
    var request_6 = function (e) {
        state = 0;
        query = $('a#sendbox6').text();
        $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix right"><img src="/img/user.png" alt="User Avatar" class="mfr circle responsive-img" align="right"><p class="right">' + query + '</p></div></li>');
        $(".panel-body").stop().animate({
            scrollTop: $(".panel-body")[0].scrollHeight
        }, 1000);
        function response() {
            if (state == 0) {
                $(".panel-body").stop().animate({
                    scrollTop: $(".panel-body")[0].scrollHeight
                }, 1000);
            }
        }
        setTimeout(response, 1000);
    };

    var request_7 = function (e) {
        state = 0;
        query = $('a#sendbox7').text();
        $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix right"><img src="/img/user.png" alt="User Avatar" class="mfr circle responsive-img" align="right"><p class="right">' + query + '</p></div></li>');
        $(".panel-body").stop().animate({
            scrollTop: $(".panel-body")[0].scrollHeight
        }, 1000);
        function response() {
            if (state == 0) {
                $(".panel-body").stop().animate({
                    scrollTop: $(".panel-body")[0].scrollHeight
                }, 1000);
            }
        }
        setTimeout(response, 1000);
    };

    var request_8 = function (e) {
        state = 0;
        query = $('a#sendbox8').text();
        $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix right"><img src="/img/user.png" alt="User Avatar" class="mfr circle responsive-img" align="right"><p class="right">' + query + '</p></div></li>');
        $(".panel-body").stop().animate({
            scrollTop: $(".panel-body")[0].scrollHeight
        }, 1000);
        function response() {
            if (state == 0) {
                $(".panel-body").stop().animate({
                    scrollTop: $(".panel-body")[0].scrollHeight
                }, 1000);
            }
        }
        setTimeout(response, 1000);
    };
    var request_9 = function (e) {
        state = 0;
        query = $('a#sendbox9').text();
        $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix right"><img src="/img/user.png" alt="User Avatar" class="mfr circle responsive-img" align="right"><p class="right">' + query + '</p></div></li>');
        $(".panel-body").stop().animate({
            scrollTop: $(".panel-body")[0].scrollHeight
        }, 1000);
        function response() {
            if (state == 0) {
                $(".panel-body").stop().animate({
                    scrollTop: $(".panel-body")[0].scrollHeight
                }, 1000);
            }
        }
        setTimeout(response, 1000);
    };
    var request_10 = function (e) {
        state = 0;
        query = $('a#sendbox10').text();
        $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix right"><img src="/img/user.png" alt="User Avatar" class="mfr circle responsive-img" align="right"><p class="right">' + query + '</p></div></li>');
        $(".panel-body").stop().animate({
            scrollTop: $(".panel-body")[0].scrollHeight
        }, 1000);
        function response() {
            if (state == 0) {
                $(".panel-body").stop().animate({
                    scrollTop: $(".panel-body")[0].scrollHeight
                }, 1000);
            }
        }
        setTimeout(response, 1000);
    };
    var request_11 = function (e) {
        state = 0;
        query = $('a#sendbox11').text();
        $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix right"><img src="/img/user.png" alt="User Avatar" class="mfr circle responsive-img" align="right"><p class="right">' + query + '</p></div></li>');
        $(".panel-body").stop().animate({
            scrollTop: $(".panel-body")[0].scrollHeight
        }, 1000);
        function response() {
            if (state == 0) {
                $(".panel-body").stop().animate({
                    scrollTop: $(".panel-body")[0].scrollHeight
                }, 1000);
            }
        }
        setTimeout(response, 1000);
    };


	var submit_form = function(e) {
		$.getJSON($SCRIPT_ROOT + '/_add_numbers', {
			query: query,
		}, function(data) {
			speak(data.result)
            $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix left"><img src="/img/AIWISFIN.png" alt="User Avatar" class="mfr circle responsive-img" align="left"><p class="left">' + data.result + '</p></div></li>');
			$(".panel-body").stop().animate({
				scrollTop: $(".panel-body")[0].scrollHeight
			}, 2000);
			$('input[name=query]').focus().select();
			state = 1;
		});
		return false;
	};
    var submit_form2 = function (e) {
        $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
            query: query,
        }, function (data) {
            speak(data.result)
            $(".chat").append('<li class="clearfix"><div class="message row"></div><div class="col s10 m10 l10 chat-body clearfix left"><img src="/img/AIWISFIN.png" alt="User Avatar" class="mfr circle responsive-img" align="left"><p class="left">' + data.result + '</p></div></li>');
            $(".panel-body").stop().animate({
                scrollTop: $(".panel-body")[0].scrollHeight
            }, 2000);
            state = 1;
        });
        return false;
    };
	$('a#sendbox').bind('click', function() {
		request();
		submit_form();
    });
    $('a#sendbox2').bind('click', function () {
        request_2();
        submit_form2();
    });
    $('a#sendbox3').bind('click', function () {
        request_3();
        submit_form2();
    });
    $('a#sendbox4').bind('click', function () {
        request_4();
        submit_form2();
    });

    $('a#sendbox5').bind('click', function () {
        request_5();
        submit_form2();
    });
    $('a#sendbox6').bind('click', function () {
        request_6();
        submit_form2();
    });
    $('a#sendbox7').bind('click', function () {
        request_7();
        submit_form2();
    });
    $('a#sendbox8').bind('click', function () {
        request_8();
        submit_form2();
    });
    $('a#sendbox9').bind('click', function () {
        request_9();
        submit_form2();
    });
    $('a#sendbox10').bind('click', function () {
        request_10();
        submit_form2();
    });
    $('a#sendbox11').bind('click', function () {
        request_11();
        submit_form2();
    });


    
	$('input[type=text]').bind('keydown', function(e) {
		if (e.keyCode == 13) {
			request();
			submit_form(e);
			e.preventDefault();
		}
	});

	$('input[name=query]').focus();
	var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
	var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent;

	function testSpeech() {
		$('#voiceBtn').disabled = true;
		$('#voice_icon').css({
			transition: 'color 1s ease',
			color:'#c21830',
		});

		var recognition = new SpeechRecognition();
		recognition.lang = 'zh-Hant-TW';
		recognition.interimResults = false;
		recognition.maxAlternatives = 1;

		recognition.start();

		recognition.onresult = function(event) {
			// The SpeechRecognitionEvent results property returns a SpeechRecognitionResultList object
			// The SpeechRecognitionResultList object contains SpeechRecognitionResult objects.
			// It has a getter so it can be accessed like an array
			// The first [0] returns the SpeechRecognitionResult at position 0.
			// Each SpeechRecognitionResult object contains SpeechRecognitionAlternative objects that contain individual results.
			// These also have getters so they can be accessed like arrays.
			// The second [0] returns the SpeechRecognitionAlternative at position 0.
			// We then return the transcript property of the SpeechRecognitionAlternative object
			var speechResult = event.results[0][0].transcript;
			$('#input_text').val(speechResult);
			request();
			submit_form();
			console.log('Confidence: ' + event.results[0][0].confidence);
		}

		recognition.onspeechend = function() {
			recognition.stop();
			$('#voice_icon').css('color', 'white', '!important');
			$('#voiceBtn').disabled = false;
		}

		recognition.onerror = function(event) {
			$('#voiceBtn').disabled = false;
			$('#voiceBtn').textContent = 'Start new test';
			$('#input_text').val('Error occurred in recognition: ' + event.error);
		}

	}

	$('#voiceBtn').click(function() {
		testSpeech()
	});
});
