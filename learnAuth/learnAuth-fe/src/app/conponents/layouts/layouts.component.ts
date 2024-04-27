import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-layouts',
  templateUrl: './layouts.component.html',
  styleUrl: './layouts.component.scss'
})
export class LayoutsComponent {

  constructor(private router:Router) { }
  logout(){
    localStorage.removeItem('token');
    this.router.navigate(['/login']);
  }
}
