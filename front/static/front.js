const payment_json = document.getElementById("pagamento").innerHTML;
const cancel_json = document.getElementById("cancelamento").innerHTML;
var meuBotao_GET = document.getElementById("btn_get");
var meuBotao_POST = document.getElementById("btn_post");

const lbl_skt = document.getElementById("sck_cnt");
const back_end_url = "localhost:5000"

meuBotao_GET.addEventListener("click", function() {
  $.get(back_end_url+"/", {teste: 123})
  // fetch(host_url + "/").then(r => { console.log('foi')})
  // fetch(host_url+"/", {
  //   method: "GET",
  //   headers: {
  //     "Content-Type": "application/json",
  //   },body: {teste: 123}
  // }).then(r  => {
  //   console.log('GET')
  // });
  // alert("GET");
});

meuBotao_POST.addEventListener("click", function() {
  $.post(back_end_url+"/", {teste: 123},function (data){
    console.log("teste123")
  })
  // fetch(host_url+"/", {
  //   method: "POST",
  //   headers: {
  //     "Content-Type": "application/json",
  //   },body: {teste: 123}
  // }).then(r  => {
  //   console.log('POST')
  // });
  // alert("POST");
});
