const meuBotao_btn_socket = document.getElementById("btn_socket");
const meuBotao_btn_socket_disconnect = document.getElementById("btn_socket_disconnect");
var meuBotao_GET = document.getElementById("btn_get");
var meuBotao_POST = document.getElementById("btn_post");

const lbl_skt = document.getElementById("sck_cnt");
const back_end_url = "localhost:5000"

meuBotao_btn_socket.addEventListener("click", function() {
  const socket = io(back_end_url);
  socket.on('connect', () => {
    // Envia mensagem de autorização para o servidor
    socket.emit('authorization', { token: 'erg8e1b6r8g46e4rmzer46g8he1ntb6jytkkorytjdhs8kuy64tjyr5the1g' });
  });

  socket.on('authorization_response', (response) => {
    if (response.success) {
      lbl_skt.innerHTML = "Conectado"
      // Autorização bem sucedida, pode usar o socket agora

      console.log('Conectado')
    } else {
      // Autorização falhou, desconecta o socket
      lbl_skt.innerHTML = "Conectado"
      socket.disconnect();
    }
  });

  socket.io.on('transport:before', (data) => {
    data.xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
  });
});

meuBotao_btn_socket_disconnect.addEventListener("click", function() {
  const socket = io(back_end_url);
  socket.on('disconnect', () => {
    // Envia mensagem de autorização para o servidor
    socket.emit('client_disconnecting', { token: 'erg8e1b6r8g46e4rmzer46g8he1ntb6jytkkorytjdhs8kuy64tjyr5the1g' });
  });

  // Trata a resposta do servidor
  socket.on('disconnect_response', (response) => {
    if (response.success) {
      // Autorização bem sucedida, pode usar o socket agora
      lbl_skt.innerHTML = "Desconectado"
      console.log('Desconectado')
    } else {
      // Autorização falhou, desconecta o socket
      console.log('Erro')
      socket.disconnect();
    }
  });

  // Adiciona o cabeçalho Access-Control-Allow-Origin em todas as solicitações
  socket.io.on('transport:before', (data) => {
    data.xhr.setRequestHeader('Access-Control-Allow-Origin', '*');
  });
});

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
