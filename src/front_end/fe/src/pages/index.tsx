import React, { useEffect } from "react";
import { Box } from "theme-ui";
import getHome from "../service/getHome";
import {GetServerSideProps} from "next";
import { METHODS } from "http";


// type Props = {
//   dataBook:any | undefined;
// }

// export const getServerSideProps: GetServerSideProps<Props> = async () => {
//   const resDataBook = getHome.getAll()
//   return{
//     props: {
//       dataBook:resDataBook
//     }
//   }
// }

const Home = () => {
  useEffect(() => {
    getHome.getAll().then(res => {
      console.log(res.data)
    }).catch(err => {
      console.log(err.message)
    })
    
  }, [])
  return(
    <Box>hahaha</Box>
  );
}
export default Home;