import axios from 'axios'
import React,{useState,useEffect} from 'react'
import Styles from "./Blog.module.css"
import InputModal from './InputModal'
import ModalBox from './ModalBox'

function Timeline() {
    const [Modal, setModal] = useState(false)
    const [data,setData] = useState()
    const [ShowInput, setShowInput] = useState(false)
    const [relod,setRelod] = useState(false)
    const [customerBlog,setCustomerBlog] = useState([])

    const addData =(item)=>{
        setData(item)
        setModal(true)
    }

    useEffect(() => {
        axios.get(`https://oyster-app-7ulvb.ondigitalocean.app/blog/list/view/customer/`)
        .then((response)=>{
            setCustomerBlog(response.data)
        })
    }, [relod])

  return (
    <div className={Styles.timeline}>
        <div className={Styles.timelinePost}>
            <div className={Styles.topuserImg}>
                <img className="rounded rounded-pill" src="image/user/user.webp" alt=""/>
            </div>
            <div className={Styles.input}>
                <input type="text" placeholder="whats's on your mind?" onClick={()=>setShowInput(true)}/>
            </div>
            {ShowInput && <InputModal setShowInput={setShowInput} setRelod={setRelod}/>}
        </div>
        <div className="row">
            {
                customerBlog.map((item,index)=>{
                    return(
                        <div className='col-md-4' key={index}>
                            <div onClick={()=>addData(item)} className={Styles.timelineBox}>
                                <div className={Styles.timelineItem}>
                                    <img className={Styles.blogImg} src={item.image} alt="" />
                                    <div className={Styles.blogItemContent}>
                                        {/* <div className={Styles.title}>
                                            <h3>{item.title}</h3>
                                        </div> */}
                                        <div className={Styles.user}>
                                            <div className={Styles.userImg}>
                                                <img className="rounded rounded-pill" src="image/user/user.webp" alt=""/>
                                            </div>
                                            <h3>{item.title}</h3>
                                        </div>
                                        <div className={Styles.userName}>
                                            <h5>Jon Deo</h5>
                                        </div>
                                        <div className={Styles.dec}>
                                            <p>{item.description.slice(0,130)}</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )
                })
            }

            {
                Modal && (<div className={Styles.Modal}>
                <ModalBox item={data} setModal={setModal}/>
                </div>)
            }

        </div>
    </div>
  )
}

export default Timeline

