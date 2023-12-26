import authFormClasses from "./AuthForm.module.css";
import wavePattern from "../../../assets/wavePattern.png";
import { useRef, useState } from "react";
import Input from "../../common/Input/Input";

const AuthForm = ({ isLogin }) => {
  const headerTitle = isLogin ? "Here you can Login" : "Here you can Sign up";
  const headerMessage = isLogin ? "Welcome back :)" : "Let's join us";
  const submitButtonText = isLogin ? "Login" : "Sign up";
  const otherOptionText = isLogin ? "Sign up" : "Login";
  const otherOptionLink = isLogin ? "/signUp" : "/login";

  const usernameInputRef = useRef(null);
  const passwordInputRef = useRef(null);

  return (
    <div className={authFormClasses.container}>
      <a className={authFormClasses.otherOptionButton} href={otherOptionLink}>
        {otherOptionText}
        <ion-icon name="arrow-forward-outline"></ion-icon>
      </a>

      <div className={authFormClasses.content}>
        <header className={authFormClasses.header}>
          <h1 className={authFormClasses.header__title}>{headerTitle}</h1>
          <h3 className={authFormClasses.header__message}>{headerMessage}</h3>
        </header>

        <form className={authFormClasses.form}>
          <ul className={authFormClasses.form__controlGroups}>
            <li className={authFormClasses.form__controlGroup}>
              <label
                className={authFormClasses.controlGroup__label}
                for="username"
              >
                Username
              </label>
              <Input type="text" ref={usernameInputRef} id="username" />
            </li>

            <li className={authFormClasses.form__controlGroup}>
              <label
                className={authFormClasses.controlGroup__label}
                for="password"
              >
                Password
              </label>
              <Input type="password" id="password" ref={passwordInputRef} />
            </li>
          </ul>

          <button className={authFormClasses.form__submitButton}>
            {submitButtonText}
          </button>
        </form>
      </div>

      <div className={authFormClasses.wavePattern__container}>
        <img
          className={authFormClasses.wavePattern}
          alt="dark wave pattern"
          src={wavePattern}
        />
      </div>
    </div>
  );
};

export default AuthForm;
