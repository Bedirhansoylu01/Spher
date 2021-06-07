import React, { useState, useEffect } from 'react'
import { apiShareList } from './lookup'
import { Share } from './detail'

export function ShareList(props) {

    const [sharesInit, setSharesInit] = useState([])
    const [shares, setShares] = useState([])
    const [shareDidSet, setShareDidSet] = useState(false)


    useEffect(() => {
        const final = [...props.newShares].concat(sharesInit)
        if (final.length !== shares.length) { // consistent loop  can`t sees likes
            setShares(final)
        }
    }, [props.newShares, shares, sharesInit])



    useEffect(() => {
        if (shareDidSet === false) {
            const handleShareListLookup = (response, status) => {
                if (status === 200) {

                    setSharesInit(response)
                    setShareDidSet(true)

                } else {
                    alert('There was an error')
                }
            }
            apiShareList(props.username, handleShareListLookup)
        }
    }, [sharesInit, shareDidSet, setShareDidSet, props.username])//if second argument only is sharesInit consistent loop begin 


    const handleDidRecommit = (newShare) => {
        const updateSharesInit = [...sharesInit]
        updateSharesInit.unshift(newShare)
        setSharesInit(updateSharesInit)
        const updateFinalShares = [...shares]
        updateFinalShares.unshift(shares)
        setShares(updateFinalShares)


    }

    return shares.map((item, index) => {
        return <Share share={item}
            didRecommit={handleDidRecommit}
            className='col-12 col-md-10 mx-auto border rounded py-3 mb-4'
            key={`${index}`} />
    }

    )
}