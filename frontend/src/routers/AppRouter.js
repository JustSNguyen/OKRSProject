import { Route, Navigate, Routes } from "react-router-dom";
import LoginForm from "../components/auth/loginForm/LoginForm";
import SignUpForm from "../components/auth/signUpForm/SignUpForm";

const AppRouter = () => {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/signUp" replace />} />
      <Route path="/login" element={<LoginForm />} />
      <Route path="/signUp" element={<SignUpForm />} />
      <Route path="*" element={<h1>NOT FOUND</h1>} />
    </Routes>
  );
};

export default AppRouter;
