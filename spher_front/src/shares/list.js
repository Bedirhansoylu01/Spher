import React, { useState, useEffect } from 'react'
import { apiShareList } from './lookup'
import { Share } from './detail'

export function ShareList(props) {

    const [sharesInit, setSharesInit] = useState([])
    const [shares, setShares] = useState([])
    const [nextUrl,setNextUrl] = useState(null)
    const [sharesDidSet, setShareDidSet] = useState(false)


    useEffect(() => {
        const final = [...props.newShares].concat(sharesInit)
        if (final.length !== shares.length) { 
            setShares(final)
        }
    }, [props.newShares, shares, sharesInit])



    useEffect(() => {
        if (sharesDidSet === false){
            const handleShareListLookup = (response, status) => {
                if (status === 200) {
                    setNextUrl(response.next)
                    setSharesInit(response.results)
                    setShareDidSet(true)
                    console.log(response)
                } else {
                    alert('There was an error')
                }
            }
            apiShareList(props.username, handleShareListLookup)
        }
    }, [sharesInit, sharesDidSet, setShareDidSet, props.username])//if second argument only is sharesInit consistent loop begin 


    const handleDidRecommit = (newShare) => {
        const updateSharesInit = [...sharesInit]
        updateSharesInit.unshift(newShare)
        setSharesInit(updateSharesInit)
        const updateFinalShares = [...shares]
        updateFinalShares.unshift(shares)
        setShares(updateFinalShares)
    }
    const handleLoadNext=(event)=>{
        event.preventDefault()
        if (nextUrl !== null){
            const handleLoadNextResponse=(response,status)=>{if (status === 200) {
                setNextUrl(response.next)
                const newShares=[...shares].concat(response.results)
                setSharesInit(newShares)
                setShares(newShares)
            } else {
                alert('There was an error')
            }
        }
            apiShareList(props.username,handleLoadNextResponse,nextUrl)
        }
    }

    return <React.Fragment>{shares.map((item, index) => {
        return <Share share={item}
            didRecommit={handleDidRecommit}
            className='my-5 py-5 border bg-white text-dark'
            key={`${index}-{item.id}`} />
    })}
    { nextUrl !== null && <button onClick={handleLoadNext} className='btn btn-outline-primary' >Load next</button>}
    </React.Fragment> }
