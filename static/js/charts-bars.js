/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */

const mydata = JSON.parse(document.getElementById('chart_data').textContent);

const barConfig = {
  type: 'bar',
  data: {
    labels: mydata['labels'],
    datasets: [
      {
        label: 'Contactos',
        backgroundColor: '#680e91ff',
        // borderColor: window.chartColors.red,
        borderWidth: 1,
        data: mydata['data'],
      },
    ],
  },
  options: {
    responsive: true,
    legend: {
      display: false,
    },    
  },
}

const barsCtx = document.getElementById('bars')
window.myBar = new Chart(barsCtx, barConfig)
