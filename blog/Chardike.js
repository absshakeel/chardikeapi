import React,{useState} from 'react'
import Styles from "./Blog.module.css"
import CModalBox from './CModalBox'

function Chardike({addBlog}) {
    const [Modal, setModal] = useState(false)
    const [data,setData] = useState()

    const addData =(item)=>{
        setData(item)
        setModal(true)
    }
  return (
        <div className="row">
        {
            addBlog.map((item,index)=>{
                return(
                    <div className='col-md-4' key={index}>
                        <div onClick={()=>addData(item)} className={Styles.timelineBox}>
                            <div className={Styles.timelineItem}>
                                <img className={Styles.blogImg} src={item.image} alt="" />
                                <div className={Styles.blogItemContent}>
                                    <div className={Styles.title}>
                                        <h3>{item.title}</h3>
                                    </div>
                                    <p>{item.description.slice(0,130)}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                )
            })
        }

        {
            Modal && (<div className={Styles.Modal}>
            <CModalBox item={data} setModal={setModal}/>
            </div>)
        }

    </div>
  )
}

export default Chardike