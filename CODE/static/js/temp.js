    function getResponse() {
        let userText = $("#textInput").val();
        data = {
            "intents": [{
                    "tag": "greeting",
                    "patterns": ["hi", "how are you", "is anyone there?", "hello", "hey", "good day", "whats up"],
                    "responses": ["Hello!", "Good to see you again!", "Hey!", "Hello there", "Hello again", "Hey there"],
                    "context_set": ""
                },
                {
                    "tag": "goodbye",
                    "patterns": ["cya", "see you later", "goodbye", "i am leaving", "have a Good day", "bye"],
                    "responses": ["Sad to see you go..", "Talk to you later", "Goodbye!"],
                    "context_set": ""
                }, {
                    "tag": "yes",
                    "patterns": ["yes", "yeah", "yup", "totally", "cool", "ok", "ya"],
                    "responses": ["Ok you replied yes!", "Ok you replied yes!"],
                    "context_set": ""
                }, {
                    "tag": "no",
                    "patterns": ["no", "na", "nope", "disagree", "nah", "nooo"],
                    "responses": ["Ok you replied no!", "Ok you replied no!"],
                    "context_set": ""
                }

            ]
        };


        let userHtml =
            '<div class="d-flex justify-content-end mb-4">\
								<div class="msg_cotainer_send">' +
            userText +
            '</div>\
		</div>';
        $("#textInput").val("");
        $("#chat-body").append(userHtml);
        // $.get("/get", { msg: userText }).done(function(data) {
        //     let botHtml =
        //         '<div class="d-flex justify-content-start mb-4">\
        //         <div class="msg_cotainer">' +
        //         data +
        //         '</div>\
        //     </div>';
        //     botdata = data;
        //     $("#chat-body").append(botHtml);
        // });


        if (data['intents'][2]['patterns'].includes(userText)) { //yes
            let length = data['intents'][2]['responses'].length
            let resp = data['intents'][2]['responses']
            let botresponse = resp[Math.floor(Math.random() * length)]
            let botHtml =
                '<div class="d-flex justify-content-start mb-4">\
                    <div class="msg_cotainer">' +
                botresponse +
                '</div>\
                </div>';
            $("#chat-body").append(botHtml);

        } else if (data['intents'][3]['patterns'].includes(userText)) { //no
            let length = data['intents'][3]['responses'].length
            let resp = data['intents'][3]['responses']
            let botresponse = resp[Math.floor(Math.random() * length)]
            let botHtml =
                '<div class="d-flex justify-content-start mb-4">\
                    <div class="msg_cotainer">' +
                botresponse +
                '</div>\
                </div>';
            $("#chat-body").append(botHtml);
        } else { //extra
            botresponse = "This is a chatbot called Evaluator. Do you want to start with the evaluation?"
            let botHtml =
                '<div class="d-flex justify-content-start mb-4">\
                    <div class="msg_cotainer">' +
                botresponse +
                '</div>\
                </div>';
            $("#chat-body").append(botHtml);
        }


        //$.get("/get", { msg: userText }).done(function(data) {
        //let botHtml =         
        //'<div class="d-flex justify-content-start mb-4">\
        //    <div class="msg_cotainer">'
        //        +data+
        //    '</div>\
        //</div>';
        //botdata = data;
        //$("#chat-body").append(botHtml);});

    }
    $("#buttonInput").click(function() {
        getResponse();
    });