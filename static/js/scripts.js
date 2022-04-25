$(document).ready(function () {
  $("#verificar").addClass("hidden");
  $("#algoritmo").change(function () {
    console.log($("#algoritmo").val());

    if (
      $("#algoritmo").val() == "amplitude" ||
      $("#algoritmo").val() == "profundidade" ||
      $("#algoritmo").val() == "profundidade_limitada" ||
      $("#algoritmo").val() == "profundidade_limitada_3" ||
      $("#algoritmo").val() == "profundidade_limitada_4" ||
      $("#algoritmo").val() == "aprofundamento_iterativo"
    ) {
      $("#origem_primeiro_metodo").addClass("hidden");
      $("#origem_segundo_metodo").removeClass("hidden");
      $("#verificar").removeClass("hidden");
      $("#verificar").attr("disabled", "true");
      $("#algoritmo").addClass("hidden");
      $("#destino_1").removeClass("hidden");
      $("#origem_1").removeClass("hidden");
      $("#origem_2").removeClass("hidden");
    } else {
      $("#verificar").removeClass("hidden");
      $("#verificar").attr("disabled", "true");
      $("#algoritmo").addClass("hidden");
      $("#destino").removeClass("hidden");
      $("#origem").removeClass("hidden");
    }
  });
  $("#destino").change(function () {
    $("#verificar").attr("disabled", false);
  });
  $("#destino_1").change(function () {
    $("#verificar").attr("disabled", false);
  });
});
