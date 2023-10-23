

function getMonthValue() {
  var uiMonth = document.getElementsByName("uiMonth");
  for(var i in uiMonth) {
    if(uiMonth[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; 
}

function onClickedEstimatequality() {
  console.log("Estimate quality button clicked");
  // ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity

  var ph = document.getElementById("uiph");
  var hardness = document.getElementById("uihardness");
  var solids = document.getElementById("uisolids");
  var chloramines = document.getElementById("uichloramines");
  var sulfate = document.getElementById("uisulfate");
  var conductivity = document.getElementById("uiconductivity");
  var organic_carbon = document.getElementById("uiorganic_carbon");
  var trihalomethanes = document.getElementById("uitrihalomethanes");
  var turbidity = document.getElementById("uiturbidity");



console.log(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity)
console.log("data ")
  var url = "http://127.0.0.1:5000/predict_quality";
  $.post(url, {
      ph: parseFloat(ph.value),
      hardness: parseFloat(hardness.value),
      solids: parseFloat(solids.value),
      chloramines: parseFloat(chloramines.value),
      sulfate: parseFloat(sulfate.value),
      conductivity: parseFloat(conductivity.value),
      organic_carbon: parseFloat(organic_carbon.value),
      trihalomethanes: parseFloat(trihalomethanes.value),
      turbidity: parseFloat(turbidity.value),

  },function(data, status) {
      console.log("data recieved from model");
      console.log(typeof(data.estimated_quality));
      console.log(data.estimated_quality);
      // uiWaterQuality
      if(data.estimated_quality == 0){
        uiWaterQuality.innerHTML = "<h2>Water is Unsafe!!!</h2>";
      }
      else{
        uiWaterQuality.innerHTML = "<h2>Water is safe!</h2>";
      }
      console.log(status);

  });
  console.log("sent details")
}

function onPageLoad() {
  console.log( "document loaded yoo" );
  var url = "http://127.0.0.1:5000/get_response"; 
  $.get(url,function(data, status) {
      console.log("got response  request");
  });
}

window.onload = onPageLoad;
