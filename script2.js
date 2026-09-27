document.addEventListener('DOMContentLoaded', () => {

    // get references to all elements
    const datetimeEl = document.getElementById('datetime');
    const cryptoData = document.getElementById('crypto-data');
    const quoteData = document.getElementById('quote-data');
    const refreshCrypto = document.getElementById('refresh-crypto');
    const refreshQuote = document.getElementById('refresh-quote');
    const notesArea = document.getElementById('notes');
    const saveNotes = document.getElementById('save-notes');

    // function to update the date and time display
    function updateDateTime() {
        const now = new Date();
        datetimeEl.textContent = now.toLocaleString();
    }

    // update time every second
    setInterval(updateDateTime, 1000);
    updateDateTime();

    // function to fetch crypto prices from coingecko api
    async function fetchCrypto() {
        cryptoData.textContent = 'loading...';
        try {
            // fetch bitcoin and ethereum prices in usd
            const response = await fetch(
                'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd'
            );
            const data = await response.json();

            // build html to display prices
            cryptoData.innerHTML = `
                <div class="price-row">
                    <span>bitcoin</span>
                    <span>$${data.bitcoin.usd.toLocaleString()}</span>
                </div>
                <div class="price-row">
                    <span>ethereum</span>
                    <span>$${data.ethereum.usd.toLocaleString()}</span>
                </div>
            `;
        } catch (error) {
            // handle any errors that occur during fetch
            cryptoData.textContent = 'failed to load prices. check your connection.';
            console.error('crypto fetch error:', error);
        }
    }

    // function to fetch a random quote
    async function fetchQuote() {
        quoteData.textcontent = 'loading...';
        try {
            const response = await fetch('https://dummyjson.com/quotes/random');
            const data = await response.json();

            // display quote and author
            quoteData.innerHTML = `
                <p>"${data.content}"</p>
                <p style="margin-top: 10px; color: #94a3b8;">— ${data.author}</p>
            `;
        } catch (error) {
            quoteData.textContent = 'failed to load quote.';
            console.error('quote fetch error:', error);
        }
    }

    // save notes to localstorage
    saveNotes.addEventListener('click', () => {
        localStorage.setItem('dashboard-notes', notesArea.value);
        saveNotes.textContent = 'saved!';
        setTimeout(() => {
            saveNotes.textContent = 'save';
        }, 1500);
    });

    // load saved notes when page opens
    const savedNotes = localStorage.getItem('dashboard-notes');
    if (savedNotes) {
        notesArea.value = savedNotes;
    }

    // attach event listeners to refresh buttons
    refreshCrypto.addEventListener('click', fetchCrypto);
    refreshQuote.addEventListener('click', fetchQuote);

    // load initial data when page opens
    fetchCrypto();
    fetchQuote();

});