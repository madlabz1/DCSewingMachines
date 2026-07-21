// DC Sewing Machines - Client-side Interactive Logic

document.addEventListener('DOMContentLoaded', () => {
    // Page-specific module initializations
    if (document.getElementById('chat-messages')) {
        initChatbot();
    }
    
    if (document.getElementById('repair-booking-form')) {
        initBooking();
    }
    
    if (document.querySelector('.filters-sidebar')) {
        initShopFilters();
    }
    
    if (document.querySelector('.grid-products')) {
        initProductRedirects();
    }
});

/* ==========================================================================
   Chatbot Module (Digital Technical Assistant)
   ========================================================================== */
function initChatbot() {
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const sendBtn = document.getElementById('chat-send');
    const suggestionsContainer = document.querySelector('.chat-suggestions');

    // Engineering Q&A Database
    const knowledgeBase = [
        {
            keys: ['needle', 'denim', 'jeans', 'heavy'],
            answer: "For denim, canvas, or heavy fabrics, do NOT use standard universal needles—they will bend and slip stitches. You need a size 90/14 or 100/16 Jeans (Denim) needle. It has a reinforced blade and a very sharp point to pierce dense weave without damage. We sell these directly on our Shopify store!"
        },
        {
            keys: ['bobbin', 'pfaff', 'passport', 'metal'],
            answer: "Careful with Pfaff Passport bobbins! They use specific plastic bobbins with a slight concave centre. Never use generic flat metal bobbins in them; you'll damage the hook race and mess up your tension. Look for Pfaff Category J bobbins on our Shopify store. We sell them pre-bundled in our Essentials Kit."
        },
        {
            keys: ['tension', 'bunching', 'nesting', 'looping'],
            answer: "If you have a 'bird's nest' of thread underneath your fabric, 9 times out of 10 it's actually the TOP thread that isn't tensioned properly. Raise your presser foot, re-thread the top path completely making sure it sits deep in the tension discs, then lower the foot and try again. If it still nests, your bobbin case might have lint. Blow it out!"
        },
        {
            keys: ['brother', 'fs40', 'e6', 'error'],
            answer: "Getting an E6 error on a Brother FS40? That means your motor is overloaded or the thread is caught in the hook area. Turn off the machine, remove the needle plate, slide out the bobbin case, and clear any thread nest or dust bunnies. Spin the handwheel toward you manually to ensure it moves freely before powering back on."
        },
        {
            keys: ['service', 'repair', 'clean', 'oil'],
            answer: "Standard household machines need a service every 12 to 18 months to clean out lint and oil the internal gears. You can book a service slot with our 3rd-party technician network using our online scheduler."
        },
        {
            keys: ['price', 'cost', 'fee', 'charge'],
            answer: "A standard sewing machine service is £75. Minor adjustments like timing issues or tension corrections run around £45. Major electrical or motor repairs start from £120. Check out our booking calculator to get an instant quote."
        },
        {
            keys: ['advisor', 'owner', 'who are you', 'expert'],
            answer: "I am the Digital Technical Assistant for DC Sewing Machines. I have been trained on our engineering logs and service guides compiled by our Head Advisor, Don Campbell, who has over 35 years of machine maintenance experience."
        }
    ];

    const defaultResponses = [
        "That's a good question! I recommend checking your threading first. If it's a model-specific question, try typing in brand names like 'Brother', 'PFAFF', or ask about 'bobbin matching'.",
        "Interesting issue. Most sewing machine glitches are caused by lint in the hook area or an old needle. Try replacing the needle first. If you need a professional look, you can schedule an appointment on the right!",
        "If it is a mechanical timing issue, it's best to book a service with one of our certified 3rd-party mobile technicians using our online scheduler."
    ];

    function addMessage(text, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.classList.add('msg', sender === 'bot' ? 'msg-bot' : 'msg-user');
        msgDiv.textContent = text;
        chatMessages.appendChild(msgDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    function handleSend() {
        const query = chatInput.value.trim().toLowerCase();
        if (!query) return;

        addMessage(chatInput.value, 'user');
        chatInput.value = '';

        // Simulate typing delay
        setTimeout(() => {
            let matchedAnswer = null;
            
            for (const item of knowledgeBase) {
                if (item.keys.some(key => query.includes(key))) {
                    matchedAnswer = item.answer;
                    break;
                }
            }

            if (matchedAnswer) {
                addMessage(matchedAnswer, 'bot');
            } else {
                const randomDefault = defaultResponses[Math.floor(Math.random() * defaultResponses.length)];
                addMessage(randomDefault, 'bot');
            }
        }, 600);
    }

    sendBtn.addEventListener('click', handleSend);
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSend();
    });

    // Handle suggestion button clicks
    suggestionsContainer.addEventListener('click', (e) => {
        if (e.target.classList.contains('btn-suggestion')) {
            chatInput.value = e.target.textContent;
            handleSend();
        }
    });
}

/* ==========================================================================
   Booking Module (Repair Booking System)
   ========================================================================== */
function initBooking() {
    const repairTypeSelect = document.getElementById('repair-type');
    const serviceMethodSelect = document.getElementById('service-method');
    const bookingSummary = document.getElementById('booking-summary');
    const bookingForm = document.getElementById('repair-booking-form');

    const pricing = {
        'standard': 75,
        'tension': 45,
        'motor': 120
    };

    function updatePrice() {
        const type = repairTypeSelect.value;
        const method = serviceMethodSelect.value;

        if (!type || !method) {
            bookingSummary.style.display = 'none';
            return;
        }

        let basePrice = pricing[type] || 0;
        let serviceCharge = method === 'mobile' ? 15 : 0; // Mobile travel surcharge
        let total = basePrice + serviceCharge;

        // Populate summary
        bookingSummary.innerHTML = `
            <p><span>Repair Service:</span> <span>£${basePrice.toFixed(2)}</span></p>
            ${method === 'mobile' ? '<p><span>Mobile Travel Surcharge:</span> <span>£15.00</span></p>' : '<p><span>Drop-off Fee:</span> <span>£0.00</span></p>'}
            <p><span>Total Estimated Cost:</span> <span>£${total.toFixed(2)}</span></p>
        `;
        bookingSummary.style.display = 'block';
    }

    repairTypeSelect.addEventListener('change', updatePrice);
    serviceMethodSelect.addEventListener('change', updatePrice);

    bookingForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const type = repairTypeSelect.value;
        const method = serviceMethodSelect.value;
        const name = document.getElementById('cust-name').value;

        if (!type || !method || !name) {
            alert('Please fill out all fields before booking.');
            return;
        }

        let successMessage = '';
        if (method === 'mobile') {
            successMessage = `Thank you, ${name}! Your booking has been received. A certified 3rd-party mobile technician has been notified and will contact you within 24 hours to confirm the repair appointment.`;
        } else {
            successMessage = `Thank you, ${name}! Your slot is reserved. You will receive an email shortly with your drop-off code for the secure lobby locker at 1774 Pershore Rd. The repair will be serviced by a certified 3rd-party engineering partner.`;
        }

        alert(successMessage);
        bookingForm.reset();
        bookingSummary.style.display = 'none';
    });
}

/* ==========================================================================
   Shop Filters Module (Category & Price Filtering)
   ========================================================================== */
function initShopFilters() {
    const filterButtons = document.querySelectorAll('.btn-filter');
    const cards = document.querySelectorAll('#catalog-products .card');

    let activeCategory = 'all';
    let activePriceRange = 'all';

    filterButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const parent = e.target.parentElement;
            
            // Toggle active state in the siblings
            parent.querySelectorAll('.btn-filter').forEach(sibling => {
                sibling.classList.remove('active');
            });
            e.target.classList.add('active');

            // Determine if category or price was clicked
            if (e.target.hasAttribute('data-category')) {
                activeCategory = e.target.getAttribute('data-category');
            } else if (e.target.hasAttribute('data-price')) {
                activePriceRange = e.target.getAttribute('data-price');
            }

            filterProducts();
        });
    });

    function filterProducts() {
        cards.forEach(card => {
            const category = card.getAttribute('data-category');
            const price = parseFloat(card.getAttribute('data-price'));

            let matchCategory = (activeCategory === 'all' || category === activeCategory);
            let matchPrice = true;

            if (activePriceRange === 'under-50') {
                matchPrice = (price < 50);
            } else if (activePriceRange === '50-300') {
                matchPrice = (price >= 50 && price <= 300);
            } else if (activePriceRange === 'over-300') {
                matchPrice = (price > 300);
            }

            if (matchCategory && matchPrice) {
                card.style.display = 'flex';
            } else {
                card.style.display = 'none';
            }
        });
    }
}

/* ==========================================================================
   Product Redirect Alerts (Shopify/Stan Store Redirection)
   ========================================================================== */
function initProductRedirects() {
    const productGrids = document.querySelectorAll('.grid-products');
    
    productGrids.forEach(grid => {
        grid.addEventListener('click', (e) => {
            const btn = e.target.closest('.btn-add-cart');
            if (btn) {
                const card = btn.closest('.card');
                const productName = card.querySelector('h3').textContent;
                const platform = btn.textContent.includes('Shopify') ? 'Shopify' : 'Stan Store';
                
                alert(`Redirecting to our secure ${platform} product page for "${productName}"...`);
            }
        });
    });
}
