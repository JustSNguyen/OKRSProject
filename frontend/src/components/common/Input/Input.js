import inputClasses from "./Input.module.css";

const Input = ({ type, ref, id, placeholder = "" }) => {
  return (
    <input
      ref={ref}
      type={type}
      id={id}
      placeholder={placeholder}
      className={inputClasses.input}
    />
  );
};

export default Input;
