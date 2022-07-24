import React from 'react'
import { TiDeleteOutline } from 'react-icons/ti';
import Styles from "./Blog.module.css"

function ModalBox({item,setModal}) {
  return (
    <div className={Styles.modalBox}>
        <div className={Styles.ModalBoxItem}>
            <div className={Styles.profile}>
              <div className={Styles.user}>
                  <div className={Styles.userImg}>
                      <img className="rounded rounded-pill" src="image/user/user.webp" alt=""/>
                  </div>
                  <h4>Jon Deo</h4>
              </div>
              <div onClick={()=>setModal(false)} className={Styles.close}>
                 <a className="remove-item"><TiDeleteOutline /></a> 
              </div>
            </div>
            <div className={Styles.ModaltimelineItem}>
                <img  src={item.image} alt="" />
                <div className={Styles.ModalblogItemContent}>
                    <div className={Styles.Modaltitle}>
                        <h3 className='mt-3'>{item.title}</h3>
                        <p>{item.description}</p>
                    </div>
                </div>
            </div>
        </div>           
    </div>
  )
}

export default ModalBox