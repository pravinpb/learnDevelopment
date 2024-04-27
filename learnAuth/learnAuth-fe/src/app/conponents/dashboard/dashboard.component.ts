import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss'
})
export class DashboardComponent {
constructor(private http: HttpClient, private router: Router) { 
  if (localStorage.getItem('token') == null) {
    this.router.navigate(['/login']);
  } 
  this.loadTask();



}
loadTask() {
  this.http.get('http://localhost:5000/dashboard').subscribe({
      next: (response: any) => {
          console.log(response); 
          response.forEach((item: any) => {
            for (let key in item) {
              id:key[0]
              task:key[1]
              status:key[2]
            }
            console.log(id,task,status)
          }); 
      } 
  });
}
    }
