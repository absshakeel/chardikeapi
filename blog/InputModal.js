import React, { useState } from "react";
import Styles from "./Blog.module.css";
import { TiDeleteOutline } from "react-icons/ti";
import axios from "axios";
import { toast } from 'react-hot-toast';

function InputModal({ setShowInput,setRelod }) {
  const [pic, setPic] = useState();
  const [title, setTitle] = useState("");
  const [dec, setDec] = useState("");
  const [url, setUrl] = useState("");
  const [err,setErr] = useState()
  console.log(err)
  async function SendData() {

    if(pic==="" || title==="" || dec==="" || url===""){
      toast.error("Field Must Not Be Empty")
    }else{
      const data = {
        title: title,
        description: dec,
        image: pic,
        url_field: url,
        user: localStorage.getItem("profile_ID"),
        is_active:true,
      };
      const formData = new FormData();
      for (const item in data) {
        formData.append(item, data[item]);
      }
  
      
      axios
        .post(
          "https://oyster-app-7ulvb.ondigitalocean.app/blog/create/",
          formData
        )
        .then((response) => {
          console.log(response.status);
          if(response.status){
            toast.success('Successfully Posted')
            setShowInput(false)
            setRelod(true) 
          }
        })
        .catch((error) => {
          console.log(error);
          setErr("Please input valid Data")
        });
    }
    
  }

  return (
    <div className={Styles.inputModal}>
      <div className={Styles.inputModalItem}>
        <div onClick={() => setShowInput(false)} className={Styles.Inputclose}>
          <a className="remove-item">
            <TiDeleteOutline />
          </a>
        </div>
        <p className={Styles.error}>{err}</p>
        <div className={Styles.upImg}>
          <label for="img">
            <img
              // src="image/user/user.webp"
              src={pic ? URL.createObjectURL(pic) : "logo/blogadd.png"}
              alt=""
            />
          </label>
          <input
            id="img"
            type="file"
            style={{display:"none"}}
            onChange={(e) => setPic(e.target.files[0])}
          />
        </div>
        <input
          className={Styles.topInput}
          type="text"
          name={title}
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Enter Title"
        />
        <textarea
          className={Styles.textarea}
          value={dec}
          name={dec}
          onChange={(e) => setDec(e.target.value)}
          placeholder="Enter Description"
        ></textarea>
        <input
          className={Styles.topInput}
          type="url"
          value={url}
          name={url}
          onChange={(e) => setUrl(e.target.value)}
          placeholder="Enter URL"
        />
        <button onClick={SendData}>Post</button>
      </div>
    </div>
  );
}

export default InputModal;
