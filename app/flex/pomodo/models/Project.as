package pomodo.models {
  import org.ruboss.collections.ModelsCollection;
  import org.ruboss.models.RubossModel;
  
  [Resource(name="projects")]
  [Bindable]
  public class Project extends RubossModel {
    public static const LABEL:String = "name";

    public var name:String = "";

    public var notes:String = "";

    public var startDate:Date = new Date;

    public var endDate:Date = new Date;

    public var completed:Boolean = false;

    [BelongsTo]
    public var account:Account;

    [HasMany]
    public var tasks:ModelsCollection;
    
    public function Project() {
      super(LABEL);
    }
  }
}
