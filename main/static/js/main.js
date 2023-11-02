Date.prototype.getWeek = function() {
    let date = new Date(this.getTime());
    date.setHours(0, 0, 0, 0);

    date.setDate(date.getDate() + 3 - (date.getDay() + 6) % 7);

    let week1 = new Date(date.getFullYear(), 0, 4);

    return 1 + Math.round(((date.getTime() - week1.getTime()) / 86400000
        - 3 + (week1.getDay() + 6) % 7) / 7);
}

// Returns the four-digit year corresponding to the ISO week of the date.
Date.prototype.getWeekYear = function() {
    let date = new Date(this.getTime());
    date.setDate(date.getDate() + 3 - (date.getDay() + 6) % 7);
    return date.getFullYear();
}

let date = new Date();
let currYear = date.getFullYear();
let currMonth = date.getMonth();
let currWeek = date.getWeek();
let num_week = 0;
let curr_num_week = 0;

currMonth += 1;

function createCalendar(elem, year, month, week){
    elem = document.getElementById(elem);
    let mon = month - 1;
    let d = new Date(year, mon);
    week = d.getWeek();
    let monthArr = [
        'Январь',
        "Февраль",
        "Март",
        "Апрель",
        "Май",
        "Июнь",
        "Июль",
        "Август",
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь",
    ];
    let table = `
       <caption>${monthArr[month-1]} ${year}</caption>
       <table>
           <tr>
               <th>№</th>
               <th>Пн</th>
               <th>Вт</th>
               <th>Ср</th>
               <th>Чт</th>
               <th>Пт</th>
               <th>Сб</th>
               <th>Вс</th>
           </tr>
           <tr>
    `
    let monthPrefix = new Date(year, month-1, 0).getDay();

    let pass_prefix = 0;

    for (let i=0; i<5; i++)
    {
        for (let j=0; j<8; j++)
        {
            if (j === 0){
                if (d.getWeek() === currWeek){
                    table += '<td class="curr-week">'+ d.getWeek() +'</td>';
                    num_week += 1;
                    curr_num_week = num_week;
                    console.log(num_week);

                }
                else{
                    table += '<td>'+ d.getWeek() +'</td>';
                    num_week += 1;
                }
            }

            else{
                if (j < monthPrefix+1 && pass_prefix === 0){
                    table += '<td></td>';
                }
                else{
                    table += '<td>'+ d.getDate() +'</td>';
                    d.setDate(d.getDate()+1);
                }
            }
        }
        pass_prefix = 1;
        table += '</tr><tr>'
    }


    table += '</tr></table>';
    elem.innerHTML = table;
}


function getDay(date){
    let day = date.getDay();
    if (day === 0) day = 7;
    return day - 1;
}

createCalendar('right-menu-calendar', 2023, currMonth, currWeek);

let nextBtn = document.getElementById("next");
nextBtn.addEventListener("click", function (){
    if (curr_num_week % 5 === 0){
        currWeek += 1;
        createCalendar('right-menu-calendar', currYear, currMonth+1, currWeek);
        currMonth += 1;
        num_week = 0;
    }
    else{
        currWeek += 1;
        createCalendar('right-menu-calendar', currYear, currMonth, currWeek);
    }

});

let prevBtn = document.getElementById("prev");
prevBtn.addEventListener("click", function (){
    if (curr_num_week % 5 === 1){
        currWeek -= 1;
        createCalendar('right-menu-calendar', currYear, currMonth-1, currWeek);
        currMonth -= 1;
        num_week = 0;
    }
    else{
        currWeek -= 1;
        createCalendar('right-menu-calendar', currYear, currMonth, currWeek);
    }

    console.log(curr_num_week);
});

