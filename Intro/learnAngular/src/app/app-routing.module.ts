import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CourcesComponent } from './cources/cources.component';
import { ContactComponent } from './contact/contact.component';
import { AboutComponent } from './about/about.component';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
  { path: '', component: HomeComponent},
  { path: 'cources', component: CourcesComponent },
  { path: 'contact', component: ContactComponent },
  { path: 'about', component: AboutComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
