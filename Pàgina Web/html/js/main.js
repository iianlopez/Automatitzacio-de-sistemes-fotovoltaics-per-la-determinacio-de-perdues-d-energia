var placa = new Array();
var sensor = new Array();
var dates = new Array();


(function($) {
    // USE STRICT
    "use strict";

    try {
        /* */
        /* Grafica Placa */

        function graficaPlaca(idPlaca) {
            $.ajax({
                url: 'php/controller.php',
                type: "POST",
                data: { funcio: "get_info_placa_sensor", placa: idPlaca },
                dataType: "json",
                success: function(resposta) {
                      console.log(resposta);

                    $.each(resposta, function(data, dades) {
                        /*              console.log(data);

                                      console.log(dades[idPlaca]); //Dades de la placa seleccionada.
                                      console.log(dades[1]); //Dades del sensor per calibrar
                        */

                        dates.push(data) //Guardem les dates.

                        if (dades[idPlaca] !== undefined) {
                            placa.push((dades[idPlaca])); //Guardem els valor de la placa selecionada
                        } else { //Si no tingues registre, posara un 0 per defecte
                            placa.push(0);
                        }
                        if (dades[1] !== undefined) {
                            sensor.push((dades[1])); //Guardem els valors del sensor de control.
                        } else { //Si no tingues registre, posara un 0 per defecte
                            sensor.push(0);
                        }
                    });


                    var maxNumSensor = Math.max.apply(null, sensor);
                    var maxNumPlaca = Math.max.apply(null, placa);
                    var escalaGrafica = Math.max(maxNumPlaca, maxNumSensor);



                    // Recent Report
                    const brandProduct = 'rgba(0,181,233,0.8)'
                    const brandService = 'rgba(0,173,95,0.8)'

                    
                    /* var elements = 10
                     var data1 = [52, 60, 55, 50, 65, 80, 57, 70, 105, 115]
                     var data2 = [102, 70, 80, 100, 56, 53, 80, 75, 65, 90]*/

                    var ctx = document.getElementById("recent-rep-chart");
                    if (ctx) {
                        ctx.height = 250;
                        var myChart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: dates,
                                datasets: [{
                                        label: 'Real',
                                        backgroundColor: brandService,
                                        borderColor: 'transparent',
                                        pointHoverBackgroundColor: '#fff',
                                        borderWidth: 0,
                                        data: placa

                                    },
                                    {
                                        label: 'Estimada',
                                        backgroundColor: brandProduct,
                                        borderColor: 'transparent',
                                        pointHoverBackgroundColor: '#fff',
                                        borderWidth: 0,
                                        data: sensor

                                    }
                                ]
                            },
                            options: {
                                maintainAspectRatio: true,
                                legend: {
                                    display: false
                                },
                                responsive: true,
                                scales: {
                                    xAxes: [{
                                        gridLines: {
                                            drawOnChartArea: true,
                                            color: '#f2f2f2'
                                        },
                                        ticks: {
                                            fontFamily: "Poppins",
                                            fontSize: 12
                                        }
                                    }],
                                    yAxes: [{
                                        ticks: {
                                            beginAtZero: true,
                                            maxTicksLimit: 5,
                                            stepSize: escalaGrafica / 10, //Dividim entre 10 per tindre 10 marques a la grafica
                                            max: escalaGrafica,
                                            fontFamily: "Poppins",
                                            fontSize: 12
                                        },
                                        gridLines: {
                                            display: true,
                                            color: '#f2f2f2'

                                        }
                                    }]
                                },
                                elements: {
                                    point: {
                                        radius: 0,
                                        hitRadius: 10,
                                        hoverRadius: 4,
                                        hoverBorderWidth: 3
                                    }
                                }


                            }
                        });
                    }


                },
                error: function(resposta) {
                    alert("ERROR AJAX");
                    console.log("ERROR AJAX");
                    console.log(resposta);
                }
            });
        }
        graficaPlaca(2);
        console.log(placa);
        console.log(sensor);
        console.log(dates);



        // Percent Chart
        var ctx = document.getElementById("percent-chart");
        if (ctx) {
            ctx.height = 280;
            var myChart = new Chart(ctx, {
                type: 'doughnut',
                data: {
                    datasets: [{
                        label: "My First dataset",
                        data: [60, 40],
                        backgroundColor: [
                            '#00b5e9',
                            '#fa4251'
                        ],
                        hoverBackgroundColor: [
                            '#00b5e9',
                            '#fa4251'
                        ],
                        borderWidth: [
                            0, 0
                        ],
                        hoverBorderColor: [
                            'transparent',
                            'transparent'
                        ]
                    }],
                    labels: [
                        'Products',
                        'Services'
                    ]
                },
                options: {
                    maintainAspectRatio: false,
                    responsive: true,
                    cutoutPercentage: 55,
                    animation: {
                        animateScale: true,
                        animateRotate: true
                    },
                    legend: {
                        display: false
                    },
                    tooltips: {
                        titleFontFamily: "Poppins",
                        xPadding: 15,
                        yPadding: 10,
                        caretPadding: 0,
                        bodyFontSize: 16
                    }
                }
            });
        }

    } catch (error) {
        console.log(error);
    }

})(jQuery);


(function($) {
    // USE STRICT
    "use strict";
    $(".animsition").animsition({
        inClass: 'fade-in',
        outClass: 'fade-out',
        inDuration: 900,
        outDuration: 900,
        linkElement: 'a:not([target="_blank"]):not([href^="#"]):not([class^="chosen-single"])',
        loading: true,
        loadingParentElement: 'html',
        loadingClass: 'page-loader',
        loadingInner: '<div class="page-loader__spin"></div>',
        timeout: false,
        timeoutCountdown: 5000,
        onLoadEvent: true,
        browser: ['animation-duration', '-webkit-animation-duration'],
        overlay: false,
        overlayClass: 'animsition-overlay-slide',
        overlayParentElement: 'html',
        transition: function(url) {
            window.location.href = url;
        }
    });
})(jQuery);
