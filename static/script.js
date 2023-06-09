
    function checkCardType() {
        var card = document.getElementsByName("card")[0].value;
        var firstDigits = card.substring(0, 2);
        var type = "card type"

        if (firstDigits == "51" || firstDigits == "52" || firstDigits == "53" || firstDigits == "54" || firstDigits == "55") {
            document.getElementsByClassName("card_number")[0].style.backgroundImage = "url('/static/mastercard.png')";
            
           
        } else if (firstDigits == "41" || firstDigits == "42" || firstDigits == "43" || firstDigits == "44" || firstDigits == "45") {
            document.getElementsByClassName("card_number")[0].style.backgroundImage = "url('/static/visa.png')";
            
        }
        else if(card.length === 1 || card.length === 0) {
            document.getElementsByClassName("card_number")[0].style.backgroundImage = "url('/static/card icon.svg')";
        }
        const input = document.getElementsByClassName("card_number")[0];
        input.addEventListener("input", () => input.value = formatNumber(input.value.replaceAll(" ", "")));

        const formatNumber = (number) => number.split("").reduce((seed, next, index) => {
            if (index !== 0 && !(index % 4)) seed += " ";
            return seed + next;
            }, "");
    }
   
    