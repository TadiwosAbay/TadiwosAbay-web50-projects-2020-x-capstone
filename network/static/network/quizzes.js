document.addEventListener('DOMContentLoaded', function() {
     document.querySelector('#savedMaterials').style.display='none';
     const save=document.querySelector('#save');
     save.style.visibility='hidden';
     

    document.querySelector('#add_quiz').onclick=function(){
       const quiz=document.querySelector('#savedMaterials');
       const input=document.createElement("textarea");
        if(document.querySelector('#savedMaterials').style.display==='none'){
        document.querySelector('#savedMaterials').innerHTML=" ";
        input.value=quiz.innerHTML;
        input.name="con";
        quiz.innerHTML="";
        quiz.appendChild(input);
        save.style.visibility='visible';
        save.disabled='true';
        quiz.onkeyup=()=>{
            if(quiz.innerHTML.length>0){
              save.disabled=false;
            }
            else{
              save.disabled=true;
            }
          }
          document.querySelector('#savedMaterials').style.display='block';
         }
        else{
            document.querySelector('#savedMaterials').style.display='none';

        }



    document.querySelector('#save').onclick=function(){
      document.querySelector('#quizzes').innerHTML=" ";
        fetch(`seeingMats/${input.value}`)
        .then(response=>response.json())
        .then(assis=>{
          document.querySelector('#savedMaterials').innerHTML+="<br>";
          for (i in assis.assis){
            document.querySelector('#quiz').style.display = 'none';
            console.log(assis.assis[i]);
            document.querySelector('#savedMaterials').innerHTML+=(assis.assis[i]);
            document.querySelector('#savedMaterials').innerHTML+="<br>"
        }
        })
        document.querySelector('#quizzes').style.display = 'block';
        save.style.visibility='hidden';
    }
}


  document.querySelector('#see').onclick=function(){
    document.querySelector('#quizzes').innerHTML=" ";
        fetch(`seeingMats/seeAll`)
        .then(response=>response.json())
        .then(assis=>{
          document.querySelector('#quizzes').innerHTML+="<br>";
          const quizzes=document.querySelector('#quizzes')
          for (i in assis.assis){
            console.log(assis.assis[i]);
            quizzes.innerHTML+=(assis.assis[i]);
            quizzes.innerHTML+="<br>";
         }
        document.querySelector('#quizzes').style.display = 'block';
        })

}





document.querySelector('#registered').onclick=function(){
  document.querySelector('#quizzes').innerHTML=" ";

  fetch('TeacherRegistered')
  .then(response=>response.json())
  .then(collects=>{
    document.querySelector('#quizzes').innerHTML+="<br>";
    for (j in collects.collects){
    document.querySelector('#quizzes').innerHTML+=collects.collects[j];
    document.querySelector('#quizzes').innerHTML+="<br>";
  }
  })
}

document.querySelector('#texts').onclick=function(){
  document.querySelector('#quizzes').innerHTML=" ";
  fetch('receivingComments')
  .then(response=>response.json())
  .then(messag=>{
    console.log(messag);
    const all_messag=messag;
    console.log(all_messag);
    const messages=messag.messag;
    document.querySelector('#quizzes').innerHTML+="<br>";
    for (i=0;i<messages.length;i++){
      if (messages[i].sender.is_student){
      document.querySelector('#quizzes').innerHTML+=messages[i].content;
        console.log(messages[i].content);
        document.querySelector('#quizzes').innerHTML+="<br>"
      }
    }
  })
}

document.querySelector('#sendMessage').onclick=function(){
  document.querySelector('#MessageTotheAdmin').style.display = 'block';
  document.querySelector('#MessageTotheAdmin').style.animationPlayState='running';
  }
  document.querySelector('#ff').onsubmit = function() {
          const name = document.querySelector('#adminMessage').value;
          fetch(`commentsByTeacher/${name}`)
                 .then(response=>response.json())
                 .then(messag=>{
                   alert(`${messag.messag}`)
                 })

             }


    });
