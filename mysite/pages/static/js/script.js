document.getElementById('scrollButton').addEventListener('click', function() {
    // Прокрутка к секции с классом "features"
    document.querySelector('.features').scrollIntoView({ behavior: 'smooth' });
});
document.getElementById('scrollButtonPrice').addEventListener('click', function() {
    document.getElementById('pricing').scrollIntoView({ behavior: 'smooth' });
});
document.getElementById("menuToggle").addEventListener("click", function() {
    var navMenu = document.getElementById("navMenu");
    if (navMenu.style.display === "flex") {
        navMenu.style.display = "none";
    } else {
        navMenu.style.display = "flex";
    }
});


document.addEventListener('DOMContentLoaded', function() {
    const scrollButton = document.getElementById('scrollButton'); 
    const mainContent = document.querySelector('.main-content');
    const dwcElements = document.querySelectorAll('.DWC');

    // Изменение цвета текста при наведении на кнопку
    scrollButton.addEventListener('mouseover', function() {
        dwcElements.forEach(function(dwc) {
            dwc.style.color = '#010407'; // Цвет при наведении на кнопку
            dwc.style.setProperty('color', '#010407'); // Использование !important
        });
        mainContent.style.background = 'linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(205,17,17,1) 59%, rgba(0,212,255,1) 100%)'; // Измените на желаемый цвет
    });

    // Возврат цвета при выходе курсора
    scrollButton.addEventListener('mouseout', function() {
        dwcElements.forEach(function(dwc) {
            dwc.style.color = ''; // Возврат к исходному цвету
        });
        mainContent.style.background = 'linear-gradient(90deg, rgba(2,0,36,1) 0%, rgba(10,1,1,1) 59%, rgba(2,0,36,1) 100%)'; // Возвращаем к исходному фону
    });

    // Скроллинг вниз при нажатии на кнопку
    scrollButton.addEventListener('click', function() {
        window.scrollTo({
            top: document.querySelector('.features').offsetTop,
            behavior: 'smooth'
        });
    });
    
});




// Essential Cookie: Cache page data for faster load times
function setPageCache(data) {
    document.cookie = `pageData=${encodeURIComponent(data)}; path=/; max-age=3600`; // Cache for 1 hour
}

function getPageCache() {
    let pageData = document.cookie.replace(/(?:(?:^|.*;\s*)pageData\s*\=\s*([^;]*).*$)|^.*$/, "$1");
    return pageData ? decodeURIComponent(pageData) : null;
}

// Analytics Cookie: Track user visit timestamp and page visits
function setAnalyticsCookie() {
    let visitTime = new Date().toISOString();
    document.cookie = `lastVisit=${visitTime}; path=/; max-age=31536000`; // Store for 1 year
}

function getAnalyticsCookie() {
    let lastVisit = document.cookie.replace(/(?:(?:^|.*;\s*)lastVisit\s*\=\s*([^;]*).*$)|^.*$/, "$1");
    if (lastVisit) {
        console.log(`Last visit was on ${lastVisit}`);
    } else {
        console.log("This is your first visit.");
    }
}

// Example: Set and get visit time for analytics purposes
setAnalyticsCookie();
getAnalyticsCookie();
