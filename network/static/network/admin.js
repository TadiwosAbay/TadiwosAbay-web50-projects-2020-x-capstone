document.addEventListener('DOMContentLoaded', function() {
  document.addEventListener('click', event => {



    const element = event.target;
    if (element.id === 'student'){
    fetch('receivingComments')
    .then(response=>response.json())
    .then(messag=>{
      document.querySelector('#newFields').innerHTML=" ";
      document.querySelector('#messages').innerHTML=" ";
        console.log(messag);
        const all_messag=messag;
        console.log(all_messag);
        const messages=messag.messag;
        for (i=0;i<messages.length;i++){
          if (messages[i].sender.is_student){
          document.querySelector('#messages').innerHTML+=messages[i].content;
            console.log(messages[i].content);
            document.querySelector('#messages').innerHTML+="<br>"
          }
        }

    })
  }
    else if(element.id==='teacher'){
      fetch('receivingComments')
      .then(response=>response.json())
      .then(messag=>{
        document.querySelector('#newFields').innerHTML=" ";
        document.querySelector('#messages').innerHTML=" ";
          console.log(messag);
          const all_messag=messag;
          console.log(all_messag);
          const messages=messag.messag;
          for (i=0;i<messages.length;i++){
            if (messages[i].sender.is_teacher){
            document.querySelector('#messages').innerHTML+=messages[i].content;
              console.log(messages[i].content);
              document.querySelector('#messages').innerHTML+="<br>"
            }
          }

      })
    }
    else if(element.id==='new'){
      fetch('newInterest')
      .then(response=>response.json())
      .then(message=>{
        document.querySelector('#messages').innerHTML=" ";
        document.querySelector('#newFields').innerHTML=" ";
        document.querySelector('#newFields').innerHTML+=message.message;
          console.log(message.message);
          document.querySelector('#newFields').innerHTML+="<br>"
      })
    }
  

});
});
