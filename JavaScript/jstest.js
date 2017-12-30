'use strict';

function sum(...rest) {
   var s,i;
   s=0;
   for(i=0;i<rest.length;i++){
      s=s+rest[i]
   }
   return s;
}

// 测试:
