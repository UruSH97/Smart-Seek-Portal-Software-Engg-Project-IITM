<script setup>
import axios from 'axios'
import { useRouter } from 'vue-router';
const router = useRouter();
const callback = (response) => {
  // This callback will be triggered when the user selects or login to
  // his Google account from the popup
  if (response) {
    console.log("Handle the response", response)
    sendCodeToBackend(response);
  }
}
async function sendCodeToBackend(code) {
  const response = await axios.post('http://127.0.0.1:8000/api/google-signin', {
    'gcode': code
  });

  // console.log('POST request response:', response.data);

  if (response.data.success === false) {
    alert(response.data.error);
  } else {
    // console.log(response.data);

    if (response && response.data) {
      const userEmail = response.data.user_data.email || '';
      if (userEmail.endsWith('@ds.study.iitm.ac.in')) {
        const userDetails = response.data.user_data;
        localStorage.setItem('userDetails', JSON.stringify(userDetails));
        localStorage.setItem('user-role', response.data.role);
        localStorage.setItem('Token', response.data.token);
        localStorage.setItem('user-id', response.data.user_id);
        if (response.data.role === 'instructor') {
          router.push('/instructordashboard');
        }
        else {
          router.push('/dashboard');
        }
      } else {
        // console.error('Login rejected: Invalid email domain.');
        alert("Please Login using Your IIT Madras Student Google Account.");
      }
    } else {
      console.error("Failed to fetch user details.");
    }
  }

}

</script>

<template>
  
  <div class=" login_background">

    <div class="signin_section d-md-flex">
      <div class="login-card" style="flex: 0 0 30%;">
        <section class="simple-signin">
          <h3 class="text-muted text-center">Sign-in</h3>
          <p class="text-muted text-center">
            Sign-in using the Google account you registered with to access your application or course dashboard.
          </p>
          <p class="text-muted text-center">
            Registered learners who have been provided with a student email ID, which is google enabled, should
            sign-in using their student email ID.
          </p>
        </section>

        <!-- Common -->
        <section class="mb-4">
          <form action="https://app.onlinedegree.iitm.ac.in/auth/login?next=" method="POST" class="form-signin">
            <div id="firebaseui-auth-container"></div>
            <GoogleLogin :callback="callback" />
            <div id="loader">Loading...</div>
          </form>
        </section>
      </div>
      <div class="d-md-block updates-card">
        <h2 class="mb-5 text-white">Latest Updates / Announcements</h2>
        <!-- Dynamic listing of updates -->
        <div id="update_list">
        </div>
      </div>
    </div>



    <div class="row d-md-block" style="background-color: white;">
      <div class="col-12 col-lg-12 col-md-12 py-4">
        <div id="testimonial_list">
          <div class="update_list mb-4">
            <div class="other-updates mt-4 mb-3">
              <h1 class="display-4 text-dark mb-4">Testimonials from our learners</h1>

              <div class="px-md-6 px-3 py-3" style="background-color: #F5F5F5;">
                <div class="text-center learner_blockquote">
                  <i class="fas fa-quote-left"></i>
                </div>

                <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel" data-interval="3000">
                  <ol class="carousel-indicators mt-6">
                    <li data-target="#carouselExampleIndicators" class="bg-secondary active" data-slide-to="0"></li>
                    <li data-target="#carouselExampleIndicators" class="bg-secondary" data-slide-to="1"></li>
                    <li data-target="#carouselExampleIndicators" class="bg-secondary" data-slide-to="2"></li>
                    <li data-target="#carouselExampleIndicators" class="bg-secondary" data-slide-to="3"></li>
                    <li data-target="#carouselExampleIndicators" class="bg-secondary" data-slide-to="4"></li>
                  </ol>
                  <div class="carousel-inner pb-6">
                    <div class="carousel-item active">
                      <p style="color: #848484;">
                        I just want to let you know that IITM and its team is doing an amazing job running this
                        program. I'm really
                        lucky to be enrolled into this program. I have never ever received replies for any
                        emails
                        within one day
                        from other universities. I know how difficultit is to reply to a lot of emails. Not only
                        that, right from
                        the program design and course content, every minute things are well planned and carried
                        out.
                        Hats off to
                        your team. Thank you for your support and guidance.
                      </p>
                      <h5 class="text-dark font-weight-bold mb-0">S Nithish Kumar </h5>
                      <div class="font-italic text-dark">
                        from Coimbatore, Tamil Nadu, India
                      </div>
                    </div>
                    <div class="carousel-item">
                      <p style="color: #848484;">
                        I would like to thank the whole team of IITM Online Degree for coming up with the
                        concept of
                        solving
                        questions with the professors. It has not only helped me in improving my performance
                        drastically in graded
                        assignments, but also it plays a relevant role in making the concepts more clear. Though
                        because of my
                        college schedule I am not able to attend all the live sessions, its recorded form is
                        proving
                        to be very
                        effective for me. A special mention for Prof.Andrew Thangaraj - his tips on problem
                        solving
                        are really
                        helpful. Once again thank you very much for understanding the requirements of the
                        students.
                      </p>
                      <div class="learner_sign">
                        <h5 class="text-dark font-weight-bold mb-0">Parth Shukla </h5>
                        <div class="font-italic text-dark">
                          from Lucknow, Uttar Pradesh, India
                        </div>
                      </div>
                    </div>
                    <div class="carousel-item">
                      <p style="color: #848484;">
                        I want to thank the team of IIT Madras who are making this Degree happen for us. I am
                        one of those students who had to face many financial and health issues in the early part
                        of their lives. And studying in IIT is only a dream for students like us. However, this
                        degree program (while maintaining the standard of IIT) has given us a chance to grow and
                        improve in our lives.
                        <br>
                        <br>
                        Also, I have personally checked many online programs by many Institutes and Universities
                        - however, none of them is so inspiring, innovative and challenging (at the same time).
                        <br>
                        <br>
                        It's such a great initiative of IIT Madras. I can't thank you enough and all the people
                        who are involved in making it happen. I want to specially thanks Prof. Andrew and Prof.
                        Pratap for clarifying all our doubts and also the professors and course support team -
                        without which I could have never qualified this process.
                      </p>
                      <div class="learner_sign">
                        <h5 class="text-dark font-weight-bold mb-0">Yash Raj Karthikey</h5>
                        <div class="font-italic text-dark">
                          from Bengaluru, Karnataka, India
                        </div>
                      </div>
                    </div>
                    <div class="carousel-item">
                      <p style="color: #848484;">
                        My name is Akriti Vishwas, I come from Lakhimpur Kheri, Uttar Pradesh.
                        <br>
                        <br>
                        I came across this online degree program on the internet. I just completed my 12th
                        standard and was enrolled in a bachelor degree in Hansraj College of Delhi University
                        pursuing physics honours. Apart from my degree I wanted to explore something new. This
                        program from such an esteemed institution like IIT MADRAS seemed exciting to me. The
                        unique program captured my attention and I enrolled for the qualifier level. The ever
                        increasing career opportunities in data science also contributed in a positive way.
                        After taking the classes from such qualified faculty, my interest in the program grew.
                        The unique pedagogy used by the teachers is what I found most engaging. The dedicated
                        support team also helped many learners like me at all times if we faced any
                        difficulties. Now, after qualifying the first level and being a student of the
                        foundational level, I am looking forward to this course and learning in a unique and
                        first of its kind way.
                      </p>
                      <div class="learner_sign">
                        <h5 class="text-dark font-weight-bold mb-0">Akriti Vishwas</h5>
                        <div class="font-italic text-dark">
                          from Lakhimpur Kheri, Uttar Pradesh, India
                        </div>
                      </div>
                    </div>
                    <div class="carousel-item">
                      <p style="color: #848484;">
                        This is Satej.
                        <br>
                        <br>
                        I want to just like appreciate the IIT team. They are doing a fabulous job. Even
                        though we haven't met, it
                        doesn't like that due to amazing interaction and course planning of Bsc course
                        of IIT Madras.
                        They are managing at such a level without disturbing the standard of IIT. Hats
                        off to the team at IIT
                        Madras.
                        <br>
                        <br>
                        Feeling proud to be a part of such a great program.
                      </p>
                      <div class="learner_sign">
                        <h5 class="text-dark font-weight-bold mb-0">Satej Sunil Zunjarrao</h5>
                        <div class="font-italic text-dark">
                          from Pune, Maharashtra, India
                        </div>
                      </div>
                    </div>
                  </div>
                  <a class="carousel-control-prev text-primary"
                    href="https://app.onlinedegree.iitm.ac.in/auth/login?next=https://app.onlinedegree.iitm.ac.in#carouselExampleIndicators"
                    role="button" data-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                  </a>
                  <a class="carousel-control-next"
                    href="https://app.onlinedegree.iitm.ac.in/auth/login?next=https://app.onlinedegree.iitm.ac.in#carouselExampleIndicators"
                    role="button" data-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                  </a>
                </div>
              </div>
              <div class="text-right my-4">
                <a href="https://study.iitm.ac.in/ds/testimonials.html" target="_blank" class="font-weight-600">
                  Read more Testimonials &#160; <i class="fas fa-chevron-right"></i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>



    <footer id="footer-dashboard " class="bg-primary py-3 d-md-block">
      <div class="container-fluid container-sm">
        <div class="h5 text-lighter">Contact Us</div>
        <div class="row pt-2 pb-2">
          <div class="col-sm-12 col-md-5 text-lighter">
            <div class="d-flex footer-text">
              <div style="flex-basis: 8%"><img style="width: 1rem"
                  src="../static/img/homepage/Footer-icon-location.svg"></div>
              <div style="flex-basis: 90%">
                IITM BS Degree Office, 3rd Floor, ICSR Building,<br> IIT Madras, Chennai - 600036
              </div>
            </div>
          </div>
        </div>
        <div class="row pt-2 pb-2">
          <div class="col-sm-12 col-md-5 text-lighter">
            <div class="d-flex footer-text">

              <div style="flex-basis: 8%"><img style="width: 1rem" src="../static/img/homepage/Footer-icon-phone.svg">
              </div>
              <div style="flex-basis: 90%">

                7850-999966 (Mon-Fri 9am-6pm)
                <br>


                support@study.iitm.ac.in

              </div>

            </div>
          </div>
        </div>
        <div class="row pt-2 pb-4 border-bottom justify-content-between">
          <div class="col-sm-12 col-md-5 text-lighter">
          </div>
          <div class="d-none d-md-block col-md-6 text-lighter align-self-end">
            <div class="d-flex justify-content-end footer-text">
              View Site Map
            </div>
            <div class="d-flex justify-content-end">
              <small>&#169; IIT Madras. All rights reserved.</small>
            </div>
          </div>
          <div class="d-md-none footer-hidden col-md-12 pt-4">
            <a class="text-decoration-none" href="https://www.facebook.com/iitmadrasbscdegree/" target="_blank">
              <img class="mr-1" src="../static/img/homepage/Footer-icon-facebook.svg" alt="fb" style="width: 2rem">
            </a>
            <a class="text-decoration-none" href="https://instagram.com/iitmadras_bsc?utm_medium=copy_link"
              target="_blank">
              <img class="mr-1" src="../static/img/homepage/Footer-icon-instagram.svg" alt="ig" style="width: 2rem">
            </a>
            <a class="text-decoration-none" href="https://twitter.com/iitmadras_bsc?s=09" target="_blank">
              <img class="mr-1" src="../static/img/homepage/Footer-icon-twitter.svg" alt="tw" style="width: 2rem">
            </a>
            <a class="text-decoration-none" href="https://www.linkedin.com/company/iit-madras-online-degree-programme"
              target="_blank">
              <img class="mr-1" src="../static/img/homepage/Footer-icon-linkedin.svg" alt="tw" style="width: 2rem">
            </a>

            <a class="text-decoration-none" href="https://wa.me/message/IVROM2UN7XIJL1" target="_blank">
              <img class="mr-1" src="../static/img/homepage/Footer-icon-whatsapp.svg" alt="tw" style="width: 2rem">
            </a>
          </div>
        </div>
        <div class="py-1 py-md-3 row justify-content-between">
          <div class="d-none d-md-block col-md-6 pt-2">

            <a class="text-decoration-none" href="https://www.facebook.com/iitmadrasbscdegree/" target="_blank">
              <img class="mr-1" src="../static/img/homepage/Footer-icon-facebook.svg" alt="fb" style="width: 2rem">
            </a>


            <a class="text-decoration-none" href="https://www.instagram.com/iitmadras_bsc/?utm_medium=copy_link"
              target="_blank">
              <img class="mr-1" src="../static/img/homepage/Footer-icon-instagram.svg" alt="ig" style="width: 2rem">
            </a>



            <a class="text-decoration-none" href="https://in.linkedin.com/company/iit-madras-bs-datascience-programme"
              target="_blank">
              <img class="mr-1" src="../static/img/homepage/Footer-icon-linkedin.svg" alt="tw" style="width: 2rem">
            </a>


            <a class="text-decoration-none" href="https://api.whatsapp.com/message/IVROM2UN7XIJL1" target="_blank">
              <img class="mr-1" src="../static/img/homepage/Footer-icon-whatsapp.svg" alt="tw" style="width: 2rem">
            </a>

          </div>
          <div class="col-sm-12 col-md-6 d-md-none footer-hidden footer-text-small text-lighter">
            <div class="d-flex justify-content-md-end footer-text">
              View Site Map
            </div>
            <div class="d-flex justify-content-md-end">
              <small>&#169; IIT Madras. All rights reserved.</small>
            </div>
          </div>
          <div class="col-sm-12 col-md-6 d-flex justify-content-md-end">
            <div class="text-lighter">
              <span class="footerLinks footer-text" url="privacy_policy.html" style="cursor: pointer;">Privacy
                Policy</span> |
              <span class="footerLinks footer-text" url="tos.html" style="cursor: pointer;">Terms of
                Service</span>
            </div>
          </div>
        </div>
      </div>
    </footer>

  </div>
</template>

<style scoped>
body {
  background-color: #f5f5f5;
}

.root {
  display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    padding-top: 40px;
    padding-bottom: 40px;
}

.form-signin {
width: 100%;
max-width: 420px;
padding: 15px;
margin: auto;
}

.form-label-group {
position: relative;
margin-bottom: 1rem;
}

.form-label-group > input,
.form-label-group > label {
height: 3.125rem;
padding: .75rem;
}

.form-label-group > label {
position: absolute;
top: 0;
left: 0;
display: block;
width: 100%;
margin-bottom: 0; /* Override default `<label>` margin */
line-height: 1.5;
color: #495057;
pointer-events: none;
cursor: text; /* Match the input under the label */
border: 1px solid transparent;
border-radius: .25rem;
transition: all .1s ease-in-out;
}

.form-label-group input::-webkit-input-placeholder {
color: transparent;
}

.form-label-group input:-ms-input-placeholder {
color: transparent;
}

.form-label-group input::-ms-input-placeholder {
color: transparent;
}

.form-label-group input::-moz-placeholder {
color: transparent;
}

.form-label-group input::placeholder {
color: transparent;
}

.form-label-group input:not(:placeholder-shown) {
padding-top: 1.25rem;
padding-bottom: .25rem;
}

.form-label-group input:not(:placeholder-shown) ~ label {
padding-top: .25rem;
padding-bottom: .25rem;
font-size: 12px;
color: #777;
}

/* Redesigned login forms */
.login_background {
  min-height: 91vh;
  overflow-x: hidden;
  background:  transparent linear-gradient(207deg, #A0322C 0%, #EBC133 100%) 0% 0% no-repeat padding-box;
}
.diploma_login_background {
  min-height: 91vh;
  overflow-x: hidden;
  background: linear-gradient(90deg, #1CB5E0 0%, #000851 100%);
}
.signin_section {
  padding: 2rem;
}
.login-card {
  border-radius: 1rem;
  background-color: white;
  max-height: 600px;
  padding: 1.5rem;
  margin: 40px;
}
.updates-card{
  margin: 40px 0 0 0;
}
.other-updates{
  padding: 60px;
}
.update_item {}

.update_item--title {
  color: white;
  font-size:16px;
  font-weight: bold;
}
.update_item--description {
  color: white;
  font-size:16px;
}
.update_item--level{
  background-color: white;font-size:14px;padding: 0 5px;border-radius: 4px;
}
@media only screen and (max-width: 1024px) {
  .signin_section {
    padding: 1.5rem;
  }
  .login-card {
    /* height: 640px; */
    margin: 0;
    padding: 1.2rem;
    font-size: 12px;
  }
  .login_background {
    height: 100vh;
  }
  .other-updates{
    padding: 1.7rem;
  }
}
@media only screen and (max-width: 769px) {
  .signin_section {
    padding: 1.5rem;
  }
  .login-card {
    /* height: 640px; */
    margin: 0;
    padding: 1rem;
    font-size: 10px;
  }
  .login_background {
    height: 100vh;
  }
  .other-updates{
    padding: 1.5rem;
  }
}
/* End of Redesigned  */

/* Redesigned login forms */
  .login_background {
    min-height: 91vh;
    overflow-x: hidden;
    background:  transparent linear-gradient(207deg, #A0322C 0%, #EBC133 100%) 0% 0% no-repeat padding-box;
  }
  .signin_section {
    padding: 2rem;
  }
  .login-card {
    border-radius: 1rem;
    background-color: white;
    max-height: 600px;
    padding: 1.5rem;
    margin: 40px;
  }
  .updates-card{
    margin: 40px 0 0 0;
  }
  .other-updates{
    padding: 60px;
  }
  .update_item {}

  .update_item--title {
    color: white;
    font-size:16px;
    font-weight: bold;
  }
  .update_item--description {
    color: white;
    font-size:16px;
  }
  .update_item--level{
    background-color: white;font-size:14px;padding: 0 5px;border-radius: 4px;
  }
  @media only screen and (max-width: 1024px) {
    .signin_section {
      padding: 1.5rem;
    }
    .login-card {
      /* height: 640px; */
      margin: 0;
      padding: 1.2rem;
      font-size: 12px;
    }
    .login_background {
      height: 100vh;
    }
    .other-updates{
      padding: 1.7rem;
    }
  }
  @media only screen and (max-width: 769px) {
    .signin_section {
      padding: 1.5rem;
    }
    .login-card {
      /* height: 640px; */
      margin: 0;
      padding: 1rem;
      font-size: 10px;
    }
    .login_background {
      height: 100vh;
    }
    .other-updates{
      padding: 1.5rem;
    }
  }
/* End of Redesigned  */

/* Fallback for Edge
-------------------------------------------------- */
@supports (-ms-ime-align: auto) {
.form-label-group > label {
  display: none;
}
.form-label-group input::-ms-input-placeholder {
  color: #777;
}
}

/* Fallback for IE
-------------------------------------------------- */
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
.form-label-group > label {
  display: none;
}
.form-label-group input:-ms-input-placeholder {
  color: #777;
}
}

</style>